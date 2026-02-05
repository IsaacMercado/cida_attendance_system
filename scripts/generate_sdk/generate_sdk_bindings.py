#!/usr/bin/env python3
"""Genera cida_attendance/sdk/_generated.py desde HCNetSDK.h usando ctypesgen.

- Headers: scripts/generate_sdk/incEn/
- Binarios: libs/

Usa CustomWrapperPrinter para:
- No imprimir srcinfo (# archivo:línea)
- Mantener el loader multiplataforma de ctypesgen
- Cargar librerías sin romper el import si un nombre no existe en la plataforma
"""

import importlib.util
import sys
from pathlib import Path

from ctypesgen import main as ctypesgen_main
from ctypesgen import printer_python


def _load_custom_printer() -> type:
    here = Path(__file__).resolve().parent
    custom_printer_path = here / "custom_printer.py"
    spec = importlib.util.spec_from_file_location("custom_printer", custom_printer_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"No se pudo cargar: {custom_printer_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.CustomWrapperPrinter


def _libraries_for_platform() -> list[str]:
    """Devuelve nombres de librerías a probar con `-l`.

    Nota: el printer custom envuelve la carga en try/except, así que podemos
    listar dependencias sin romper el import en plataformas donde no existan.

    Requisito actual: solo soportamos Linux y Windows.
    """

    if sys.platform.startswith("linux"):
        return [
            "libcrypto.so.1.1",
            "libssl.so.1.1",
            "libopenal.so.1",
            "libPlayCtrl.so",
            "libNPQos.so",
            "libAudioRender.so",
            "libSuperRender.so",
            "libHCCore.so",
            "libhpr.so",
            "libhcnetsdk.so",
        ]

    if sys.platform == "win32":
        return [
            "libcrypto-1_1-x64.dll",
            "libssl-1_1-x64.dll",
            "OpenAL32.dll",
            "zlib1.dll",
            "hlog.dll",
            "hpr.dll",
            "NPQos.dll",
            "AudioRender.dll",
            "SuperRender.dll",
            "PlayCtrl.dll",
            "HCCore.dll",
            "HCNetSDK.dll",
        ]

    raise RuntimeError(
        f"Plataforma no soportada por ahora: sys.platform={sys.platform!r}. "
        "Solo Linux y Windows."
    )


# Rutas
PROJECT_ROOT = Path(__file__).resolve().parents[2]
HEADERS_DIR = Path(__file__).parent / "incEn"
HEADER_FILE = HEADERS_DIR / "HCNetSDK.h"
OUTPUT_DIR = PROJECT_ROOT / "cida_attendance" / "sdk"
GENERATED_FILE = OUTPUT_DIR / "_generated.py"
LIBS_DIR = PROJECT_ROOT / "libs"


def generate_full_sdk():
    """Genera el SDK completo en _generated.py"""
    if not HEADER_FILE.exists():
        print(f"No existe header: {HEADER_FILE}")
        sys.exit(1)

    OUTPUT_DIR.mkdir(exist_ok=True)

    # Enganchar nuestro printer (sin crear runner separado).
    printer_python.WrapperPrinter = _load_custom_printer()

    # Ojo: listamos múltiples nombres; el printer los envuelve en try/except.
    libs = _libraries_for_platform()
    argv = [
        str(HEADER_FILE),
        "-o",
        str(GENERATED_FILE),
        "-I",
        str(HEADERS_DIR),
        "--no-macro-warnings",
        "--allow-gnu-c",
        "--runtime-libdir",
        str(LIBS_DIR),
    ]

    for lib in libs:
        argv.extend(["-l", lib])

    try:
        ctypesgen_main.main(argv)
    except SystemExit as e:
        # ctypesgen llama sys.exit internamente
        code = int(getattr(e, "code", 1) or 0)
        if code != 0:
            raise

    size_mb = GENERATED_FILE.stat().st_size / (1024 * 1024)
    print(f"Generado: {GENERATED_FILE} ({size_mb:.1f} MB)")

    # Contar funciones
    with open(GENERATED_FILE, "r") as f:
        content = f.read()

    import re

    functions = re.findall(r"(NET_DVR_\w+)\s*=", content)
    print(f"Funciones: {len(functions):,}")

    return GENERATED_FILE


def main():
    generate_full_sdk()


if __name__ == "__main__":
    main()
