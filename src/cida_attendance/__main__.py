# nuitka-project: --python-flag=-m
# nuitka-project: --windows-console-mode=attach
# nuitka-project: --include-package-data=cida_attendance
# nuitka-project: --include-package=cida_attendance.sdk.api.structs
# nuitka-project: --nofollow-import-to=tkinter

# GUI build toggle:
# - Headless/default: CIDA_GUI_BUILD unset or 0 -> excludes PySide6/shiboken6
# - GUI: set CIDA_GUI_BUILD=1 -> includes PySide6 plugin and Qt adjustments
#
# Linux/macOS:
#   CIDA_GUI_BUILD=1 uv run python -m nuitka --standalone src/cida_attendance
#
# Windows (PowerShell):
#   $env:CIDA_GUI_BUILD='1'; uv run python -m nuitka --standalone src/cida_attendance

# nuitka-project-if: __import__("os").environ.get("CIDA_GUI_BUILD", "0").lower() in ("1", "true", "yes", "on"):
#   nuitka-project: --enable-plugin=pyside6
#   nuitka-project: --noinclude-qt-translations
#   nuitka-project: --noinclude-qt-plugins=printsupport

# nuitka-project-if: __import__("os").environ.get("CIDA_GUI_BUILD", "0").lower() not in ("1", "true", "yes", "on"):
#   nuitka-project: --nofollow-import-to=PySide6
#   nuitka-project: --nofollow-import-to=shiboken6

# nuitka-project-if: {OS} == "Linux":
#   nuitka-project: --include-data-files=libs/*.so*=libs/
#   nuitka-project: --include-data-files=libs/HCNetSDKCom/*.so*=libs/HCNetSDKCom/
#   nuitka-project: --include-data-files=libs/*.xml=libs/

# nuitka-project-if: {OS} == "Windows":
#   nuitka-project: --include-data-files=libs/*.dll=libs/
#   nuitka-project: --include-data-files=libs/*.lib=libs/
#   nuitka-project: --include-data-files=libs/*.zip=libs/
#   nuitka-project: --include-data-files=libs/*.exe=libs/
#   nuitka-project: --include-data-files=libs/HCNetSDKCom/*.dll=libs/HCNetSDKCom/
#   nuitka-project: --include-data-files=libs/HCNetSDKCom/*.lib=libs/HCNetSDKCom/
#   nuitka-project: --include-data-files=libs/ClientDemoDll/*.dll=libs/ClientDemoDll/
#   nuitka-project: --include-data-files=libs/ClientDemoDll/*.txt=libs/ClientDemoDll/


from cida_attendance import cli

if __name__ == "__main__":
    cli.app()
