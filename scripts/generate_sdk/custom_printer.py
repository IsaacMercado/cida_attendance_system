from __future__ import annotations

from ctypesgen.printer_python.printer import WrapperPrinter


class CustomWrapperPrinter(WrapperPrinter):
    """Custom WrapperPrinter for this project.

    Goals:
    - Do not emit srcinfo comments (file:line).
    - Keep ctypesgen's cross-platform loader.
    - Allow multiple library names without failing import on missing ones.
    - Generate a portable runtime library search (PyInstaller/Nuitka/dev).
    """

    def print_header(self):
        # Avoid emitting absolute paths (argv/date from the default template).
        self.file.write(
            'r"""Wrapper for HCNetSDK.h\n\n'
            'Generated with:\n'
            'ctypesgen + CustomWrapperPrinter\n\n'
            'Do not modify this file.\n'
            '"""\n'
        )
        self.file.write("\n__docformat__ = \"restructuredtext\"\n")

    def srcinfo(self, src):
        # Silence all file:line references.
        return

    def print_library(self, library):
        # Do not fail import if a library name doesn't exist on this platform.
        self.file.write("try:\n")
        self.file.write(f'    _libs["{library}"] = load_library("{library}")\n')
        self.file.write("except Exception:\n")
        self.file.write("    pass\n")

    def print_loader(self):
        self.file.write("_libs = {}\n")
        self.file.write("_libdirs = %s\n\n" % self.options.compile_libdirs)
        self.file.write("# Begin loader\n\n")
        if self.options.embed_preamble:
            from ctypesgen.printer_python.printer import LIBRARYLOADER_PATH

            with open(LIBRARYLOADER_PATH, "r") as loader_file:
                self.file.write(loader_file.read())
        else:
            self.file.write("from .ctypes_loader import *\n")
        self.file.write("\n# End loader\n\n")

        self.file.write("import os\n")
        self.file.write("import sys\n\n")

        self.file.write("def _cida_candidate_library_dirs():\n")
        self.file.write("    dirs = []\n\n")
        self.file.write("    env_dir = os.environ.get('CIDA_ATTENDANCE_LIBS_DIR')\n")
        self.file.write("    if env_dir:\n")
        self.file.write("        dirs.append(env_dir)\n\n")

        self.file.write("    nuitka_temp = os.environ.get('NUITKA_ONEFILE_TEMP_DIR')\n")
        self.file.write("    if nuitka_temp:\n")
        self.file.write("        dirs.append(os.path.join(nuitka_temp, 'libs'))\n\n")

        self.file.write("    if hasattr(sys, '_MEIPASS'):\n")
        self.file.write("        dirs.append(os.path.join(sys._MEIPASS, 'libs'))\n\n")

        self.file.write("    try:\n")
        self.file.write("        exe_dir = os.path.dirname(sys.executable)\n")
        self.file.write("        if exe_dir:\n")
        self.file.write("            dirs.append(os.path.join(exe_dir, 'libs'))\n")
        self.file.write("            dirs.append(os.path.join(exe_dir, '_internal', 'libs'))\n")
        self.file.write("    except Exception:\n")
        self.file.write("        pass\n\n")

        self.file.write("    try:\n")
        self.file.write("        here = os.path.abspath(os.path.dirname(__file__))\n")
        self.file.write("        dirs.append(os.path.abspath(os.path.join(here, os.pardir, os.pardir, os.pardir, 'libs')))\n")
        self.file.write("    except Exception:\n")
        self.file.write("        pass\n\n")

        self.file.write("    # Expand base dirs to include vendor subdirs when present.\n")
        self.file.write("    expanded = []\n")
        self.file.write("    for d in dirs:\n")
        self.file.write("        expanded.append(d)\n")
        self.file.write("        expanded.append(os.path.join(d, 'HCNetSDKCom'))\n")

        self.file.write("    out = []\n")
        self.file.write("    seen = set()\n")
        self.file.write("    for d in expanded:\n")
        self.file.write("        if not d or d in seen:\n")
        self.file.write("            continue\n")
        self.file.write("        seen.add(d)\n")
        self.file.write("        if os.path.isdir(d):\n")
        self.file.write("            out.append(d)\n")
        self.file.write("    return out\n\n")

        self.file.write("add_library_search_dirs(_cida_candidate_library_dirs())\n")

    def print_fixed_function(self, function):
        # Search across all loaded libraries; avoids depending on source_library.
        self.srcinfo(function.src)

        CC = "stdcall" if function.attrib.get("stdcall", False) else "cdecl"

        self.file.write(
            "for _lib in _libs.values():\n"
            f'    if not _lib.has("{function.c_name()}", "{CC}"):\n'
            "        continue\n"
            f'    {function.py_name()} = _lib.get("{function.c_name()}", "{CC}")\n'
        )

        # Argument types
        self.file.write(
            "    %s.argtypes = [%s]\n"
            % (function.py_name(), ", ".join([a.py_string() for a in function.argtypes]))
        )

        # Return value
        if function.restype.py_string() == "String":
            self.file.write(
                "    if sizeof(c_int) == sizeof(c_void_p):\n"
                "        {PN}.restype = ReturnString\n"
                "    else:\n"
                "        {PN}.restype = {RT}\n"
                "        {PN}.errcheck = ReturnString\n".format(
                    PN=function.py_name(), RT=function.restype.py_string()
                )
            )
        else:
            self.file.write(
                "    %s.restype = %s\n" % (function.py_name(), function.restype.py_string())
            )
            if function.errcheck:
                self.file.write("    %s.errcheck = %s\n" % (function.py_name(), function.errcheck.py_string()))

        self.file.write("    break\n")

    def print_variadic_function(self, function):
        CC = "stdcall" if function.attrib.get("stdcall", False) else "cdecl"
        self.srcinfo(function.src)
        self.file.write(
            "for _lib in _libs.values():\n"
            f'    if _lib.has("{function.c_name()}", "{CC}"):\n'
            f'        _func = _lib.get("{function.c_name()}", "{CC}")\n'
            f"        _restype = {function.restype.py_string()}\n"
            f"        _errcheck = {function.errcheck.py_string()}\n"
            "        _argtypes = [{t0}]\n"
            "        {PN} = _variadic_function(_func,_restype,_argtypes,_errcheck)\n"
            "        break\n".format(
                t0=", ".join([a.py_string() for a in function.argtypes]),
                PN=function.py_name(),
            )
        )

