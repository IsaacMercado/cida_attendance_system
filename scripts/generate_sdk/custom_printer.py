from __future__ import annotations

import re

from ctypesgen.printer_python.printer import WrapperPrinter
from ctypesgen.ctypedescs import CtypesBitfield, CtypesStruct
from ctypesgen.expressions import ExpressionNode


class CustomWrapperPrinter(WrapperPrinter):
    """Custom WrapperPrinter for this project.

    Goals:
    - Do not emit srcinfo comments (file:line).
    - Keep ctypesgen's cross-platform loader.
    - Allow multiple library names without failing import on missing ones.
    - Generate a portable runtime library search (PyInstaller/Nuitka/dev).
    - Optimize struct generation (using _S helper).
    - Optimize function generation (using _F helper).
    """

    def srcinfo(self, src):
        return

    def _clean_type_str(self, type_str):
        """Removes redundant int() wrappers from array types for cleaner code."""
        # Replaces "BYTE * int(64)" with "BYTE * 64"
        return re.sub(r'\bint\((\d+)\)', r'\1', type_str)

    def print_simple_macro(self, macro):
        self.file.write(f"{macro.name} = {macro.expr.py_string(True)}")

    def print_loader(self):
        super().print_loader()

        self.file.write("import os\n")
        self.file.write("import sys\n\n")

        # --- Helper: Structs ---
        # Reduces boilerplate for struct definitions.
        self.file.write("def _S(cls, fields, pack=None, anon=None):\n")
        self.file.write("    if pack: cls._pack_ = pack\n")
        self.file.write("    if anon: cls._anonymous_ = anon\n")
        self.file.write("    cls._fields_ = fields\n")
        self.file.write("    cls.__slots__ = [n for n, *_ in fields]\n\n")

        # --- Helper: Functions ---
        # Reduces 6+ lines of setup per function to 1 line.
        # Handles stdcall/cdecl, argtypes, restype, and error checking.
        self.file.write("def _F(name, cc, res, args, err=None):\n")
        self.file.write("    if not _libs[lib_name].has(name, cc):\n")
        self.file.write("        return None\n")
        self.file.write("    func = _libs[lib_name].get(name, cc)\n")
        self.file.write("    func.argtypes = args\n")
        self.file.write("    func.restype = res\n")
        # Handle strict String return types if needed (logic from ctypesgen)
        self.file.write("    if res is String:\n")
        self.file.write("        if sizeof(c_int) == sizeof(c_void_p):\n")
        self.file.write("             func.restype = ReturnString\n")
        self.file.write("        else:\n")
        self.file.write("             func.errcheck = ReturnString\n")
        self.file.write("    if err:\n")
        self.file.write("        func.errcheck = err\n")
        self.file.write("    return func\n\n")

        # --- Helper: Variadic Functions ---
        self.file.write("def _FV(name, cc, res, args, err=None):\n")
        self.file.write("    if not _libs[lib_name].has(name, cc):\n")
        self.file.write("        return None\n")
        self.file.write("    func = _libs[lib_name].get(name, cc)\n")
        self.file.write("    return _variadic_function(func, res, args, err)\n\n")

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

        self.file.write("add_library_search_dirs(_cida_candidate_library_dirs())\n\n")

        self.file.write("if sys.platform == 'win32':\n")
        self.file.write('    lib_name = "HCNetSDK.dll"\n')
        self.file.write("elif sys.platform == 'linux':\n")
        self.file.write('    lib_name = "libhcnetsdk.so"\n')
        self.file.write("else:\n")
        self.file.write('    raise OSError(f"Unsupported platform: {sys.platform}")\n\n')

        self.file.write('_libs[lib_name] = load_library(lib_name)\n\n')

    def print_struct_members(self, struct):
        if struct.opaque:
            return

        packed = False
        aligned = 1
        if struct.attrib.get("packed", False):
            aligned = struct.attrib.get("aligned", [1])
            assert len(aligned) == 1, "cgrammar gave more than one arg for aligned attribute"
            aligned = aligned[0]
            if isinstance(aligned, ExpressionNode):
                aligned = aligned.evaluate(None)
            packed = True

        # handle unnamed fields.
        unnamed_fields = []
        names = set([x[0] for x in struct.members])
        anon_prefix = "unnamed_"
        n = 1
        for mi in range(len(struct.members)):
            mem = list(struct.members[mi])
            if mem[0] is None:
                while True:
                    name = "%s%i" % (anon_prefix, n)
                    n += 1
                    if name not in names:
                        break
                mem[0] = name
                names.add(name)
                if type(mem[1]) is CtypesStruct:
                    unnamed_fields.append(name)
                struct.members[mi] = mem

        args = []
        
        fields_str = "[\n"
        for name, ctype in struct.members:
            type_str = self._clean_type_str(ctype.py_string())
            
            if isinstance(ctype, CtypesBitfield):
                bit_width = self._clean_type_str(ctype.bitfield.py_string(False))
                fields_str += "    ('%s', %s, %s),\n" % (name, type_str, bit_width)
            else:
                fields_str += "    ('%s', %s),\n" % (name, type_str)
        fields_str += "]"
        
        args.append(fields_str)
        
        if packed:
            args.append(f"pack={aligned}")
            
        if len(unnamed_fields) > 0:
            anon_str = "[" + ", ".join(f"'{name}'" for name in unnamed_fields) + "]"
            args.append(f"anon={anon_str}")

        self.file.write(f"_S({struct.variety}_{struct.tag}, {', '.join(args)})\n")

    def print_fixed_function(self, function):
        CC = "stdcall" if function.attrib.get("stdcall", False) else "cdecl"
        
        arg_types_str = ", ".join([self._clean_type_str(a.py_string()) for a in function.argtypes])
        args_list = f"[{arg_types_str}]"
        
        restype_str = self._clean_type_str(function.restype.py_string())

        errcheck_str = "None"
        if function.errcheck:
            errcheck_str = function.errcheck.py_string()

        # Generate single line call to _F helper
        self.file.write(
            f'{function.py_name()} = _F("{function.c_name()}", "{CC}", {restype_str}, {args_list}, {errcheck_str})\n'
        )

    def print_variadic_function(self, function):
        CC = "stdcall" if function.attrib.get("stdcall", False) else "cdecl"
        
        arg_types_str = ", ".join([self._clean_type_str(a.py_string()) for a in function.argtypes])
        args_list = f"[{arg_types_str}]"
        
        restype_str = self._clean_type_str(function.restype.py_string())
        
        errcheck_str = "None"
        if function.errcheck:
            errcheck_str = function.errcheck.py_string()

        self.file.write(
             f'{function.py_name()} = _FV("{function.c_name()}", "{CC}", {restype_str}, {args_list}, {errcheck_str})\n'
        )

    def print_variable(self, variable):
        # Optional: Optimize variable loading too if needed. 
        # For now, just standard try/except but cleaner is possible.
        # But variables are rare compared to functions in this SDK.
        super().print_variable(variable)
