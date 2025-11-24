import datetime
import os
import re
import time
from typing import Annotated

import typer
from scheduler import Scheduler

from cida_attendance.config import check_config, save_config
from cida_attendance.tasks import check_device, check_server, synchronize

app = typer.Typer()


def parse_iso8601_duration(duration: str) -> datetime.timedelta:
    pattern = r"^P(?:(?P<days>\d+\.\d+|\d*?)D)?T?(?:(?P<hours>\d+\.\d+|\d*?)H)?(?:(?P<minutes>\d+\.\d+|\d*?)M)?(?:(?P<seconds>\d+\.\d+|\d*?)S)?$"
    match = re.compile(pattern).match(duration)
    if not match:
        raise ValueError(f"Invalid ISO 8601 duration: {duration}")
    parts = {k: float(v) for k, v in match.groupdict("0").items()}
    return datetime.timedelta(**parts)


@app.command()
def server(
    with_icon: bool = False,
    interval: Annotated[str, typer.Argument(callback=parse_iso8601_duration)] = "PT1H",
    config: str = None,
    wait: float = 0.5,
):
    scheduler = Scheduler()
    scheduler.cyclic(interval, synchronize)

    if config is not None:
        os.environ["CONFIG_FILE"] = config

    typer.echo("Server started")

    if with_icon:
        from cida_attendance.gui import App

        app = App()
        app.timer.timeout.connect(lambda: scheduler.exec_jobs())
        app.timer.start(int(wait * 1000))
        app.run()
    else:
        try:
            while True:
                scheduler.exec_jobs()
                time.sleep(wait)
        except KeyboardInterrupt:
            typer.echo("Server stopped")


@app.command()
def configure(
    user: str = "admin",
    password: str = None,
    ip: str = None,
    port: int = 8000,
    uri_db: str = None,
    name: str = "",
    interative: bool = False,
    gui: bool = False,
):
    if interative and gui:
        typer.echo("Choose either interactive or gui mode")
        raise typer.Abort()

    if interative:
        user = typer.prompt("Enter the username", default=user)
        password = typer.prompt("Enter the password", hide_input=True)
        ip = typer.prompt("Enter the ip address")
        port = typer.prompt("Enter the port", type=int, default=port)
        uri_db = typer.prompt("Enter the uri database")
        name = typer.prompt("Enter the name")

    if gui:
        from PySide6.QtWidgets import QApplication

        from cida_attendance.gui import FormWindow

        app = QApplication([])
        FormWindow().show()
        app.exec_()

        if not check_config():
            typer.echo("Configuration not set up")

        return

    if password is None:
        password = typer.prompt("Enter the password", hide_input=True)

    if not all([user, password, ip, port, uri_db, name]):
        typer.echo("All fields are required")
        raise typer.Abort()

    save_config(uri_db, user, password, ip, port, name)

    typer.echo("Configuration saved")


@app.command()
def check():
    if not check_config():
        typer.echo("Configuration not set up")
        raise typer.Abort()

    if not check_server():
        typer.echo("Server not available")
        raise typer.Abort()

    check_device()
    typer.echo("Device checked")


@app.command()
def sync():
    if not check_config():
        typer.echo("Configuration not set up")
        raise typer.Abort()

    if not check_server():
        typer.echo("Server not available")
        raise typer.Abort()

    if synchronize():
        typer.echo("Synchronization finished")
    else:
        typer.echo("Synchronization failed")


if __name__ == "__main__":
    app()
