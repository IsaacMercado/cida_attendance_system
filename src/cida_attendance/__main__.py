# nuitka-project: --python-flag=-m
# nuitka-project: --enable-plugin=pyside6
# nuitka-project: --include-package-data=cida_attendance
# nuitka-project: --include-package=cida_attendance.sdk.api.structs
# nuitka-project: --include-data-files=libs/*.so*=libs/
# nuitka-project: --include-data-files=libs/HCNetSDKCom/*.so*=libs/HCNetSDKCom/
# nuitka-project: --include-data-files=libs/*.xml=libs/

from cida_attendance import cli

if __name__ == "__main__":
    cli.app()
