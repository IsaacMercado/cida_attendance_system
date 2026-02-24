# nuitka-project: --python-flag=-m
# nuitka-project: --enable-plugin=pyside6
# nuitka-project: --windows-console-mode=attach
# nuitka-project: --include-package-data=cida_attendance
# nuitka-project: --include-package=cida_attendance.sdk.api.structs
# nuitka-project: --noinclude-qt-translations
# nuitka-project: --noinclude-qt-plugins=printsupport

# nuitka-project-if: {OS} == "Linux":
#   nuitka-project: --include-data-files=libs/*.so*=libs/
#   nuitka-project: --include-data-files=libs/HCNetSDKCom/*.so*=libs/HCNetSDKCom/
#   nuitka-project: --include-data-files=libs/*.xml=libs/
#   nuitka-project: --nofollow-import-to=tkinter,unittest

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
