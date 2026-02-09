import os
from configparser import ConfigParser
from pathlib import Path

import keyring


def get_filename() -> str:
    config_file = os.getenv("CONFIG_FILE")

    if config_file is None:
        config_file = os.path.join(
            Path.home(), ".config", "cida_attendance", "config.ini"
        )

        if not os.path.exists(os.path.dirname(config_file)):
            os.makedirs(os.path.dirname(config_file))

    return config_file


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

    if config.has_option("DEFAULT", "url"):
        data["url"] = config["DEFAULT"]["url"]
    else:
        data["url"] = ""

    if config.has_option("DEFAULT", "api_key"):
        data["api_key"] = config["DEFAULT"]["api_key"]
    else:
        data["api_key"] = ""

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
    url: str,
    api_key: str,
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

    config["DEFAULT"]["url"] = url
    config["DEFAULT"]["api_key"] = api_key

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
            config.has_option("DEFAULT", "url"),
            config.has_option("DEFAULT", "api_key"),
            config.has_option("DEVICE", "user"),
            config.has_option("DEVICE", "ip"),
            config.has_option("DEVICE", "port"),
            (
                config.has_option("DEVICE", "user")
                and keyring.get_password(get_name_app(), config["DEVICE"]["user"])
            ),
        ]
    )
