import ipaddress
import logging
import platform
import socket
import time
import uuid
import xml.etree.cElementTree as etree
from concurrent.futures import ThreadPoolExecutor, as_completed

import psutil
import typer

logger = logging.getLogger(__name__)

MCAST_GRP = "239.255.255.250"
MCAST_PORT = 37020


def get_active_ipv4s():
    interfaces = psutil.net_if_addrs()
    stats = psutil.net_if_stats()

    if platform.system() == "Windows":

        def skip_interface(iface: str):
            return iface.startswith("Loopback") or not stats[iface].isup

    else:

        def skip_interface(iface: str):
            return iface == "lo" or not stats[iface].isup

    ips = []
    for iface, addrs in interfaces.items():
        if skip_interface(iface):
            continue
        for addr in addrs:
            if addr.family == socket.AF_INET:
                ips.append(addr.address)

    if ips:
        logger.info(f"Interfaces detectadas: {ips}")
    else:
        logger.warning("[-] No se encontraron IPs activas")

    return ips


def build_probe_xml() -> bytes:
    root = etree.Element("Probe")
    uuid_elem = etree.SubElement(root, "Uuid")
    uuid_elem.text = str(uuid.uuid4()).upper()
    mac_elem = etree.SubElement(root, "MAC")
    mac_elem.text = "ff-ff-ff-ff-ff-ff"
    types_elem = etree.SubElement(root, "Types")
    types_elem.text = "inquiry"

    return etree.tostring(
        root,
        method="xml",
        xml_declaration=True,
        encoding="utf-8",
    )


def find_hikvision_devices():
    ips = get_active_ipv4s()

    devices = {}
    probe_xml = build_probe_xml()

    for local_ip in ips:
        logger.info(f"--- Escaneando desde la interfaz: {local_ip} ---")
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.settimeout(3)

        try:
            # Forzamos la salida por esta interfaz específica
            sock.setsockopt(
                socket.IPPROTO_IP,
                socket.IP_MULTICAST_IF,
                socket.inet_aton(local_ip),
            )
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
            sock.sendto(probe_xml, (MCAST_GRP, MCAST_PORT))

            while True:
                data, addr = sock.recvfrom(2048)
                logger.info(f"[+] Dispositivo encontrado en IP: {addr[0]}")

                devices[addr[0]] = {
                    child.tag: child.text for child in etree.fromstring(data)
                }
        except socket.timeout:
            logger.warning("[-] No se encontraron más dispositivos en esta interfaz.")
        finally:
            sock.close()

    return devices


def listen_for_replies(sock, timeout):
    devices = {}
    end_time = time.time() + timeout
    while time.time() < end_time:
        try:
            data, addr = sock.recvfrom(4096)
        except socket.timeout:
            break
        try:
            info = {child.tag: child.text for child in etree.fromstring(data)}
        except etree.ParseError:
            continue
        ip_addr = info.get("IPv4Address", addr[0])
        devices[ip_addr] = info
    return devices


def discover_on_ip(bind_ip, timeout, broadcast_only):
    probe_xml = build_probe_xml()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.settimeout(timeout)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    sock.setsockopt(
        socket.IPPROTO_IP,
        socket.IP_MULTICAST_IF,
        socket.inet_aton(bind_ip),
    )
    sock.bind((bind_ip, MCAST_PORT))

    logger.info(f"[i] Bind IP: {bind_ip}")
    logger.info(f"[i] Bind port: {MCAST_PORT}")

    if not broadcast_only:
        sock.sendto(probe_xml, (MCAST_GRP, MCAST_PORT))
        logger.info("[>] Probe multicast enviado")

    sock.sendto(probe_xml, ("255.255.255.255", MCAST_PORT))
    logger.info("[>] Probe broadcast enviado")

    devices = listen_for_replies(sock, timeout)
    sock.close()
    return devices


def find_hikvision_devices_server_mode(bind_ip=None, timeout=4.0, broadcast_only=False):
    if bind_ip:
        bind_ips = [bind_ip]
    else:
        bind_ips = get_active_ipv4s()

    if not bind_ips:
        return

    devices = {}
    for bind_ip in bind_ips:
        devices.update(discover_on_ip(bind_ip, timeout, broadcast_only))

    if devices:
        logger.info("[+] Dispositivos encontrados:")
        for ip_addr in sorted(devices.keys()):
            logger.info(f"- {ip_addr}")
    else:
        logger.warning("[-] No se encontraron dispositivos")


def http_isapi_check(host: str, user: str, password: str, timeout: float = 10.0):
    import requests
    from requests.auth import HTTPDigestAuth

    try:
        response = requests.get(
            f"http://{host}/ISAPI/System/deviceInfo",
            auth=HTTPDigestAuth(user, password),
            timeout=timeout,
        )

        if response.status_code == 200:
            logger.info("✅ Dispositivo Activo y Autenticado")
            return etree.fromstring(response.content).tag.endswith("DeviceInfo")

        elif response.status_code == 401:
            logger.error(
                "❌ Error 401: Contraseña incorrecta o "
                "el usuario no tiene permisos ISAPI."
            )
        else:
            logger.warning(f"⚠️ Estado inesperado: {response.status_code}")

    except requests.exceptions.ConnectionError:
        logger.error("🚫 Error de conexión: No se pudo alcanzar la IP del dispositivo.")
    except requests.exceptions.RequestException as e:
        logger.error(f"❗ Ocurrió un error: {e}")

    return False


def iter_targets(entry: str):
    if "/" in entry:
        network = ipaddress.ip_network(entry, strict=False)
        for host in network.hosts():
            yield str(host)
    else:
        yield str(ipaddress.ip_address(entry))


def tcp_open(host, port, timeout):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        sock.connect((host, port))
        return True
    except OSError:
        return False
    finally:
        sock.close()


def sdk_check(host, sdk_config=None):
    if not sdk_config:
        return False

    try:
        from cida_attendance.sdk.session import Session

        config = {
            "ip": host,
            "user": sdk_config.get("user") or "",
            "password": sdk_config.get("password") or "",
            "port": sdk_config.get("port") or 8000,
        }
        with Session() as session:
            if not session.login(**config):
                return False
            try:
                payload = session.request_stdxmlconfig("GET /ISAPI/System/deviceInfo")
                return "DeviceInfo" in payload
            finally:
                session.logout()
    except Exception:
        return False


def find_hikvision_devices_by_tcp(
    target_range,
    primary_port=8000,
    extra_ports=[80, 554],
    workers=128,
    timeout=0.7,
    http_check=False,
    http_user=None,
    http_password=None,
    http_port=80,
    sdk_check=False,
):
    extra_ports = [int(p.strip()) for p in extra_ports if p.strip()]
    targets = list(iter_targets(target_range))
    logger.info(f"[i] Targets: {len(targets)}")

    candidates = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(tcp_open, host, primary_port, timeout): host
            for host in targets
        }
        for future in as_completed(futures):
            host = futures[future]
            try:
                if future.result():
                    candidates.append(host)
            except OSError:
                continue

    if not candidates:
        logger.warning("[-] Ningun host con el puerto primario abierto")
        return

    logger.info(f"[i] Candidatos con puerto {primary_port}: {len(candidates)}")

    results = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {}
        for host in candidates:
            for port in extra_ports:
                futures[executor.submit(tcp_open, host, port, timeout)] = (
                    host,
                    port,
                )
        for future in as_completed(futures):
            host, port = futures[future]
            try:
                if future.result():
                    results.append((host, port))
            except OSError:
                continue

    by_host = {}
    for host, port in results:
        by_host.setdefault(host, []).append(port)

    http_user = http_user
    http_password = http_password
    if http_check and (not http_user or not http_password):
        try:
            from cida_attendance.config import load_config

            config = load_config()
            http_user = http_user or config.get("user")
            http_password = http_password or config.get("password")
        except Exception:
            http_user = http_user or None
            http_password = http_password or None

    if http_check and (not http_user or not http_password):
        logger.warning("[!] http-check activo pero sin credenciales en config/keyring")

    sdk_config = None

    if sdk_check:
        try:
            from cida_attendance.config import load_config

            sdk_config = load_config()
        except Exception:
            sdk_config = None

        if (
            not sdk_config
            or not sdk_config.get("user")
            or not sdk_config.get("password")
        ):
            logger.warning(
                "[!] sdk-check activo pero sin credenciales en config/keyring"
            )
            sdk_config = None

    filtered = []

    for host in sorted(by_host.keys()):
        ports = sorted(set(by_host[host] + [primary_port]))

        if sdk_check:
            if not sdk_check(host, sdk_config):
                continue

        elif http_check and (http_port in ports):
            if not http_isapi_check(
                host,
                http_user,
                http_password,
                timeout=timeout + 5,
            ):
                continue

        filtered.append((host, ports))

    if filtered:
        logger.info("[+] Posibles Hikvision:")
        for host, ports in filtered:
            logger.info(f"- {host}: {ports}")
    else:
        logger.warning("[-] Sin coincidencias despues del filtro")


def main():
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )
    app = typer.Typer()

    @app.callback(invoke_without_command=True)
    def discover(ctx: typer.Context):
        devices = find_hikvision_devices()
        if devices:
            logger.info("[+] Dispositivos encontrados:")
            for ip, device in devices.items():
                logger.info(f"- {device.get('IPv4Address', 'IP desconocida')}")
        else:
            logger.warning("[-] No se encontraron dispositivos")

    @app.command()
    def server(
        bind_ip: str = typer.Option(
            None,
            help="IP local de la interfaz (ej: 10.10.0.55)",
        ),
        timeout: float = typer.Option(
            4.0,
            help="Tiempo de espera para respuestas",
        ),
        broadcast_only: bool = typer.Option(
            False,
            help="Solo envia broadcast, sin multicast",
        ),
    ):
        """Descubre Hikvision en modo servidor (UDP 37020)."""
        find_hikvision_devices_server_mode(bind_ip, timeout, broadcast_only)

    @app.command()
    def tcp(
        target_range: str = typer.Option(..., help="CIDR o IP"),
        primary_port: int = typer.Option(8000, help="Puerto primario a escanear"),
        extra_ports: str = typer.Option(
            "80,554",
            help="Puertos adicionales a escanear (separados por coma)",
        ),
        workers: int = typer.Option(128, help="Número de hilos para escaneo"),
        timeout: float = typer.Option(0.7, help="Timeout para conexiones TCP"),
        http_check: bool = typer.Option(
            False,
            help="Realiza verificación HTTP/ISAPI en hosts con puerto 80 abierto",
        ),
        http_user: str = typer.Option(None, help="Usuario HTTP/ISAPI"),
        http_password: str = typer.Option(None, help="Password HTTP/ISAPI"),
        http_port: int = typer.Option(80, help="Puerto para verificación HTTP/ISAPI"),
        sdk_check: bool = typer.Option(
            False,
            help="Valida candidatos usando el SDK (requiere credenciales en config)",
        ),
    ):
        """Descubre Hikvision por TCP con filtros para reducir falsos positivos."""
        find_hikvision_devices_by_tcp(
            target_range,
            primary_port,
            extra_ports.split(","),
            workers,
            timeout,
            http_check,
            http_user,
            http_password,
            http_port,
            sdk_check,
        )

    app()


if __name__ == "__main__":
    main()
