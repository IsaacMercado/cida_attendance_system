from pathlib import Path
from threading import Thread
from typing import TYPE_CHECKING

import pystray
from PIL import Image

from cida_attendance import tasks
from cida_attendance.config import check_config
from cida_attendance.gui import create_app

if TYPE_CHECKING:
    from pystray._base import Icon


def get_image():
    return Image.open(Path(__file__).parent / "assets" / "cida-logo.png")


def check_database(icon: "Icon", query: str) -> None:
    if not check_config():
        print("Config is not OK")
        icon.notify(
            "Required configuration is missing",
            "Please set up the configuration",
        )
        return

    print("Checking database...")

    if tasks.check_db():
        print("Database is OK")
        icon.notify("Database is OK", "Database is OK")
    else:
        print("Database is not OK")
        icon.notify(
            "Database is not OK",
            "Database is not OK",
        )


def check_device(icon: "Icon", query: str):
    if not check_config():
        print("Config is not OK")
        icon.notify(
            "Required configuration is missing",
            "Please set up the configuration",
        )
        return

    print("Checking device...")
    if tasks.check_device():
        print("Device is OK")
        icon.notify("Device is OK", "Device is OK")
    else:
        print("Device is not OK")
        icon.notify(
            "Device is not OK",
            "Device is not OK",
        )


def synchronize(icon: "Icon", query: str):
    if not check_config():
        print("Config is not OK")
        icon.notify(
            "Required configuration is missing",
            "Please set up the configuration",
        )
        return

    print("Synchronizing...")
    if tasks.synchronize():
        print("Synchronized")
        icon.notify("Synchronized", "Synchronized")
    else:
        print("Not synchronized")
        icon.notify("Not synchronized", "Not synchronized")
    print("Synchronized")


def _set_up(icon: "Icon"):
    create_app().mainloop()
    print("Set up")

    if check_config():
        icon.notify("Configuration set up", "Configuration is now set up")
    else:
        icon.notify("Configuration not set up", "Configuration is not set up")


def set_up(icon: "Icon", query: str):
    print("Setting up...")
    Thread(target=_set_up, args=(icon,)).start()


def exit(icon: "Icon", query: str):
    icon.stop()


def create_icon():
    return pystray.Icon(
        "CIDA Attendance",
        get_image(),
        "CIDA Attendance",
        menu=pystray.Menu(
            pystray.MenuItem("Check database", check_database),
            pystray.MenuItem("Check device", check_device),
            pystray.MenuItem("Synchronize", synchronize),
            pystray.MenuItem("Set up", set_up),
            pystray.MenuItem("Exit", exit),
        ),
    )


if __name__ == "__main__":
    create_icon().run()
