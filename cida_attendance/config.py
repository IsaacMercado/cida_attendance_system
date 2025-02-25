import os
from configparser import ConfigParser

import keyring


def get_filename() -> str:
    return os.getenv("CONFIG_FILE", "config.ini")


def get_name_app() -> str:
    return os.getenv("NAME_APP", "CidaAttendance")


def exists_config() -> bool:
    return os.path.exists(get_filename())


def load_config() -> dict[str, str | int]:
    config = ConfigParser()
    config.read(get_filename())

    if "DEFAULT" not in config:
        config["DEFAULT"] = {}

    if "DEVICE" not in config:
        config["DEVICE"] = {}

    data = {}

    if config.has_option("DEFAULT", "uri_db"):
        data["uri_db"] = config["DEFAULT"]["uri_db"]
    else:
        data["uri_db"] = ""

    if config.has_option("DEVICE", "user"):
        data["user"] = config["DEVICE"]["user"]
    else:
        data["user"] = ""

    if config.has_option("DEVICE", "ip"):
        data["ip"] = config["DEVICE"]["ip"]
    else:
        data["ip"] = ""

    if config.has_option("DEVICE", "port"):
        data["port"] = int(config["DEVICE"]["port"])
    else:
        data["port"] = 8000

    if config.has_option("DEVICE", "name"):
        data["name"] = config["DEVICE"]["name"]
    else:
        data["name"] = ""

    data["password"] = keyring.get_password(get_name_app(), data["user"]) or ""

    return data


def save_config(
    uri_db: str,
    user: str,
    password: str,
    ip: str,
    port: int,
    name: str,
) -> None:
    config = ConfigParser()
    config.read(get_filename())

    if not config.has_section("DEFAULT"):
        config["DEFAULT"] = {}

    config["DEFAULT"]["uri_db"] = uri_db

    if not config.has_section("DEVICE"):
        config["DEVICE"] = {}

    config["DEVICE"]["user"] = user
    config["DEVICE"]["ip"] = ip
    config["DEVICE"]["port"] = str(port)
    config["DEVICE"]["name"] = name

    with open(get_filename(), "w") as f:
        config.write(f)

    keyring.set_password(get_name_app(), user, password)


def check_config() -> bool:
    config = ConfigParser()
    config.read(get_filename())

    return all(
        [
            "DEFAULT" in config,
            "DEVICE" in config,
            config.has_option("DEFAULT", "uri_db"),
            config.has_option("DEVICE", "user"),
            config.has_option("DEVICE", "ip"),
            config.has_option("DEVICE", "port"),
            (
                config.has_option("DEVICE", "user")
                and keyring.get_password(get_name_app(), config["DEVICE"]["user"])
            ),
        ]
    )
