import sys

from cida_attendance import cli


def _attach_parent_console_if_present():
    """Attach to the parent console if one exists (Windows only).

    With a windowed executable, this mirrors Nuitka's "attach" behavior:
    - If launched from a terminal, output goes to that terminal.
    - If launched by double-click (no parent console), no console window appears.
    """
    if not sys.platform.startswith("win"):
        return
    if not getattr(sys, "frozen", False):
        return
    try:
        import ctypes

        ATTACH_PARENT_PROCESS = -1
        attached = ctypes.windll.kernel32.AttachConsole(ATTACH_PARENT_PROCESS)
        if attached:
            try:
                # Rebind stdio to the attached console
                sys.stdout = open("CONOUT$", "w", encoding="utf-8", buffering=1)
                sys.stderr = open("CONOUT$", "w", encoding="utf-8", buffering=1)
                sys.stdin = open("CONIN$", "r", encoding="utf-8")
            except Exception:
                pass
    except Exception:
        pass


if __name__ == "__main__":
    _attach_parent_console_if_present()
    cli.app()
