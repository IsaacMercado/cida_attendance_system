import datetime
import os
import re
import time
from typing import Annotated

import typer
from scheduler import Scheduler

from cida_attendance.config import check_config, save_config
from cida_attendance.core.tasks import (
    check_device,
    check_server,
    synchronize,
    synchronize_live,
)

app = typer.Typer()


def parse_iso8601_duration(duration: str) -> datetime.timedelta:
    pattern = r"^P(?:(?P<days>\d+\.\d+|\d*?)D)?T?(?:(?P<hours>\d+\.\d+|\d*?)H)?(?:(?P<minutes>\d+\.\d+|\d*?)M)?(?:(?P<seconds>\d+\.\d+|\d*?)S)?$"
    match = re.compile(pattern).match(duration)
    if not match:
        raise ValueError(f"Invalid ISO 8601 duration: {duration}")
    parts = {k: float(v) for k, v in match.groupdict("0").items()}
    return datetime.timedelta(**parts)


def _run_app(callback, wait: float = 0.5):
    from cida_attendance.ui.app import App

    app = App()
    app.timer.timeout.connect(callback)
    app.timer.start(int(wait * 1000))
    app.run()


@app.command()
def server(
    with_icon: bool = False,
    interval: Annotated[str, typer.Argument(callback=parse_iso8601_duration)] = "PT1H",
    config: str = None,
    wait: float = 0.5,
    live: bool = False,
):
    typer.echo("Starting server...")

    if config is not None:
        os.environ["CONFIG_FILE"] = config

    if live:

        def _callback():
            return synchronize() and synchronize_live(wait=wait)

        if with_icon:
            _run_app(_callback, wait)
            return

        _callback()
        return

    else:
        scheduler = Scheduler()
        scheduler.cyclic(interval, synchronize)

        def _callback():
            return scheduler.exec_jobs()

        if with_icon:
            _run_app(_callback, wait)
            return

        try:
            typer.echo("Server started")
            while True:
                _callback()
                time.sleep(wait)
        except KeyboardInterrupt:
            typer.echo("Server stopped")

    typer.echo("Server stopped")


@app.command()
def configure(
    user: str = "admin",
    password: str = None,
    ip: str = None,
    port: int = 8000,
    url: str = typer.Option(None, "--url", help="Server URL"),
    api_key: str = typer.Option(None, "--api-key", help="Server API Key"),
    name: str = "",
    interactive: bool = typer.Option(False, "--interactive"),
    gui: bool = False,
):
    if interactive and gui:
        typer.echo("Choose either interactive or gui mode")
        raise typer.Abort()

    if interactive:
        user = typer.prompt("Enter the username", default=user)
        password = typer.prompt("Enter the password", hide_input=True)
        ip = typer.prompt("Enter the ip address")
        port = typer.prompt("Enter the port", type=int, default=port)
        url = typer.prompt("Enter the server URL")
        api_key = typer.prompt("Enter the server API key")
        name = typer.prompt("Enter the name")

    if gui:
        from PySide6.QtWidgets import QApplication

        from cida_attendance.ui.app import FormWindow

        app = QApplication([])
        FormWindow().show()
        app.exec_()

        if not check_config():
            typer.echo("Configuration not set up")

        return

    if password is None:
        password = typer.prompt("Enter the password", hide_input=True)

    if not all([user, password, ip, port, url, api_key, name]):
        typer.echo("All fields are required")
        raise typer.Abort()

    save_config(url, api_key, user, password, ip, port, name)

    typer.echo("Configuration saved")


@app.command()
def check():
    if not check_config():
        typer.echo("Configuration not set up")
        raise typer.Abort()

    if not check_server():
        typer.echo("Server not available")
        raise typer.Abort()

    if not check_device():
        typer.echo("Device not available")
        raise typer.Abort()

    typer.echo("Device checked")


@app.command()
def sync(
    live: bool = typer.Option(
        False,
        "--live",
        help="Enable live synchronization",
    ),
    live_duration: float = typer.Option(
        None,
        "--live-duration",
        help="Duration for live synchronization in seconds",
    ),
    live_wait: float = typer.Option(
        0.5,
        help="Wait time between live synchronization checks in seconds",
    ),
):
    if not check_config():
        typer.echo("Configuration not set up")
        raise typer.Abort()

    if not check_server():
        typer.echo("Server not available")
        raise typer.Abort()

    typer.echo("Starting synchronization...")

    if live:
        if not synchronize():
            typer.echo("Synchronization failed")

        if synchronize_live(duration_s=live_duration, wait=live_wait):
            typer.echo("Live synchronization finished")
        else:
            typer.echo("Live synchronization failed")
    else:
        if synchronize():
            typer.echo("Synchronization finished")
        else:
            typer.echo("Synchronization failed")


if __name__ == "__main__":
    app()
