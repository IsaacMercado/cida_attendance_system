from __future__ import annotations

from ctypesgen.printer_python.printer import WrapperPrinter


class CustomWrapperPrinter(WrapperPrinter):
    """WrapperPrinter personalizado para este proyecto.

    Objetivos:
    - No imprimir comentarios srcinfo (`# archivo.h: linea`).
    - Mantener el loader multiplataforma de ctypesgen (sin duplicar loaders propios).
    - Permitir listar múltiples nombres de librería sin romper el import.
    """

    def print_header(self):
        # Evita filtrar rutas absolutas (argv/date del template default).
        self.file.write(
            'r"""Wrapper for HCNetSDK.h\n\n'
            'Generated with:\n'
            'ctypesgen + CustomWrapperPrinter\n\n'
            'Do not modify this file.\n'
            '"""\n'
        )
        self.file.write("\n__docformat__ = \"restructuredtext\"\n")

    def srcinfo(self, src):
        # Silenciar todas las referencias a archivo:línea
        return

    def print_library(self, library):
        # No fallar al importar si un nombre no existe en esta plataforma.
        self.file.write("try:\n")
        self.file.write(f'    _libs["{library}"] = load_library("{library}")\n')
        self.file.write("except Exception:\n")
        self.file.write("    pass\n")

    def print_fixed_function(self, function):
        # Forzar búsqueda en todas las librerías disponibles; evita depender de source_library.
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

