from __future__ import annotations

import re
from contextlib import contextmanager
from itertools import chain
from pathlib import Path
from typing import Generator

from ctypesgen.ctypedescs import (
    CtypesArray,
    CtypesBitfield,
    CtypesEnum,
    CtypesFunction,
    CtypesPointer,
    CtypesSimple,
    CtypesSpecial,
    CtypesStruct,
    CtypesTypedef,
)
from ctypesgen.expressions import ExpressionNode
from ctypesgen.printer_python import preamble
from ctypesgen.printer_python.printer import WrapperPrinter

HERE = Path(__file__).resolve().parent
EXTRA_FUNCTIONS_PATH = HERE / "extra_functions.py"


def _get_names(path: Path):
    names = set()

    if not path.exists():
        return names

    with path.open("r") as f:
        for line in f:
            match = re.match(r"^(\w+)\s*=\s*(\w+)", line)
            if match:
                name, _ = match.groups()
                names.add(name)

    return names


class CustomWrapperPrinter(WrapperPrinter):
    """Custom WrapperPrinter for this project."""

    _struct_data = {}
    root_path = None

    def __init__(self, outpath, options, data):
        self.root_path = Path(outpath).parent

        self.structs_path = structs_path = self.root_path / "structs"
        structs_path.mkdir(exist_ok=True)
        for struct_file in structs_path.glob("*.py"):
            struct_file.unlink()

        self.base_classes_path = self.root_path / "base_classes.py"
        if self.base_classes_path.exists():
            self.base_classes_path.unlink()

        self.base_classes_path.write_text(
            "from ctypes import Structure\n\n"
            "from .ctypes_preamble import POINTER\n\n"
            "from typing import Any\n\n"
            # --- Helper: Structs ---
            # Reduces boilerplate for struct definitions.
            "def _S(cls: Structure, fields: list[tuple[str, Any]], pack=None, anon=None):\n"
            "    if pack:\n"
            "        cls._pack_ = pack\n"
            "    if anon:\n"
            "        cls._anonymous_ = anon\n"
            "    cls._fields_ = fields\n"
            "    cls.__slots__ = [n for n, *_ in fields]\n\n"
        )

        self.constants_path = self.root_path / "constants.py"
        if self.constants_path.exists():
            self.constants_path.unlink()

        self.enums_path = enums_path = self.root_path / "enums.py"
        if enums_path.exists():
            enums_path.unlink()

        enums_path.write_text(
            "from ctypes import c_int\n\nfrom .ctypes_preamble import POINTER\n\n"
        )

        self.macros_path = self.root_path / "macros.py"
        if self.macros_path.exists():
            self.macros_path.unlink()

        self.functions_path = self.root_path / "functions.py"
        if self.functions_path.exists():
            self.functions_path.unlink()

        self.functions_path.write_text(
            "from ctypes import CFUNCTYPE\n\n"
            "from .ctypes_preamble import POINTER, UNCHECKED, String\n\n"
        )

        super().__init__(outpath, options, data)

        with structs_path.joinpath("__init__.py").open("w") as f:
            _all = []
            exports = {}

            for name, module in sorted(
                self._struct_data.items(), key=lambda x: x[::-1]
            ):
                if "ano" in name:  # Skip unnamed structs/unions.
                    continue
                _all.append(name)
                exports[name] = module

            f.write("from importlib import import_module\n\n")
            f.write("_STRUCT_EXPORTS = {\n")
            for name in sorted(_all):
                f.write(f'    "{name}": "{exports[name]}",\n')
            f.write("}\n\n")
            f.write(
                "__all__ = [\n"
                + ",\n".join(f'    "{name}"' for name in sorted(_all))
                + "\n]\n\n"
            )
            f.write(
                "def __getattr__(name: str):\n"
                "    module_name = _STRUCT_EXPORTS.get(name)\n"
                "    if module_name is None:\n"
                '        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")\n'
                '    module = import_module(f"{__name__}.{module_name}")\n'
                "    value = getattr(module, name)\n"
                "    globals()[name] = value\n"
                "    return value\n\n"
                "def __dir__():\n"
                "    return sorted(set(globals()) | set(__all__))\n"
            )

    def __del__(self):
        filename = self.file.name
        super().__del__()
        with open(filename, "r") as f:
            content = f.read()

        # Remove redundant blank lines (more than 2 in a row) for cleaner output.
        cleaned_content = re.sub(r"\n{3,}", "\n\n", content)

        with open(filename, "w") as f:
            f.write(cleaned_content)

    def print_preamble(self):
        super().print_preamble()
        self.file.write("\n")
        self.file.write(
            "from .base_classes import *\n"
            "from .constants import *\n"
            "from .enums import *\n"
            "from .functions import *\n"
            "from .structs import *\n"
            "from .macros import *\n\n"
        )

    @contextmanager
    def change_file(self, new_outpath):
        temp = self.file
        with open(new_outpath, "a", encoding="utf-8") as f:
            self.file = f
            try:
                yield
                self.file.write("\n")
            finally:
                self.file = temp

    def struct_filename(self, struct):
        filename = struct.tag.strip("_")
        if filename.startswith("tag"):
            filename = filename[3:].strip("_")
        return filename.lower()

    def module_from_type(
        self,
        ctype,
        classes_names=None,
    ) -> Generator[tuple[str, str], None, None]:
        if classes_names is None:
            classes_names = {}
            classes_names["base_classes"] = _get_names(self.base_classes_path)
            classes_names["functions"] = _get_names(self.functions_path)
            classes_names["enums"] = _get_names(self.enums_path)

        if isinstance(ctype, CtypesSimple):
            if not ctype.name == "void":
                yield ("ctypes", ctype.py_string())
        elif isinstance(ctype, CtypesStruct):
            if module_name := self._struct_data.get(f"{ctype.variety}_{ctype.tag}"):
                yield (f".{module_name}", f"{ctype.variety}_{ctype.tag}")
            else:
                raise ValueError(
                    f"Struct {ctype.variety}_{ctype.tag} not "
                    "found in _struct_data for import."
                )
        elif isinstance(ctype, CtypesArray):
            yield from self.module_from_type(ctype.base, classes_names)
        elif isinstance(ctype, CtypesPointer):
            yield from self.module_from_type(ctype.destination, classes_names)
        elif isinstance(ctype, CtypesTypedef):
            if _struct_name := self._struct_data.get(ctype.name):
                yield (f".{_struct_name}", ctype.name)
            else:
                flat = False
                for _module, _names in classes_names.items():
                    if ctype.name in _names:
                        yield (f"..{_module}", ctype.name)
                        flat = True
                        break
                if not flat:
                    print(f"Typedef {ctype.name} not found in any module for import.")
        elif isinstance(ctype, CtypesSpecial):
            if hasattr(preamble, ctype.py_string()):
                yield ("..ctypes_preamble", ctype.py_string())
            else:
                raise ValueError(
                    f"Special type {ctype.py_string()} not found in preamble."
                )
        elif isinstance(ctype, CtypesFunction):
            yield from self.module_from_type(ctype.restype, classes_names)
            for argtype in ctype.argtypes:
                yield from self.module_from_type(argtype, classes_names)
        elif isinstance(ctype, CtypesEnum):
            yield ("..enums", ctype.py_string())
        else:
            raise NotImplementedError(f"Unsupported ctype in struct members: {ctype}")

    @contextmanager
    def struct_file(self, struct):
        """Context manager to write struct members to a separate file."""
        filename = self.struct_filename(struct)
        struct_name = f"{struct.variety}_{struct.tag}"
        temp_path = self.structs_path / f"{filename}.py"

        with self.change_file(temp_path):
            yield

        # Store the temp file path for later processing in print_struct.
        self._struct_data[struct_name] = filename

    def print_macro(self, macro):
        with self.change_file(self.macros_path):
            return super().print_macro(macro)

    def print_struct(self, struct):
        with self.struct_file(struct):
            base = {"union": "Union", "struct": "Structure"}[struct.variety]
            self.file.write(f"from ctypes import {base}\n")

            for _module, _class in chain.from_iterable(
                self.module_from_type(ctype) for _, ctype in struct.members
            ):
                self.file.write(f"from {_module} import {_class}\n")

            self.file.write("from ..base_classes import _S\n")
            self.file.write("from ..ctypes_preamble import POINTER\n\n")

            self.file.write(
                "class %s_%s(%s):\n    pass\n" % (struct.variety, struct.tag, base)
            )

    def print_typedef(self, typedef):
        if isinstance(typedef.ctype, CtypesStruct):
            with self.struct_file(typedef.ctype):
                super().print_typedef(typedef)
                self._struct_data[typedef.name] = self.struct_filename(typedef.ctype)
        elif isinstance(typedef.ctype, CtypesPointer):
            if isinstance(typedef.ctype.destination, CtypesStruct):
                with self.struct_file(typedef.ctype.destination):
                    super().print_typedef(typedef)
                    self._struct_data[typedef.name] = self.struct_filename(
                        typedef.ctype.destination
                    )
            elif isinstance(typedef.ctype.destination, CtypesSimple):
                if typedef.ctype.destination.name != "void":
                    with self.base_classes_path.open("r", encoding="utf-8") as f:
                        content = f.readlines()

                    content.insert(
                        0,
                        f"from ctypes import  {typedef.ctype.destination.py_string()}\n",
                    )

                    with self.base_classes_path.open("w", encoding="utf-8") as f:
                        f.writelines(content)

                with self.change_file(self.base_classes_path):
                    super().print_typedef(typedef)

            elif isinstance(typedef.ctype.destination, CtypesEnum):
                with self.change_file(self.enums_path):
                    super().print_typedef(typedef)
            elif isinstance(typedef.ctype.destination, CtypesTypedef):
                if struct_filename := self._struct_data.get(
                    typedef.ctype.destination.name
                ):
                    with self.change_file(self.structs_path / f"{struct_filename}.py"):
                        super().print_typedef(typedef)
                    self._struct_data[typedef.name] = self._struct_data[
                        typedef.ctype.destination.name
                    ]
                else:
                    raise ValueError(
                        f"Struct {typedef.ctype.destination.name} not "
                        "found in _struct_data for import."
                    )
            else:
                raise NotImplementedError(
                    "Unsupported pointer typedef: "
                    f"{typedef.name} -> {typedef.ctype.destination}"
                )
        elif isinstance(typedef.ctype, CtypesSimple):
            if typedef.ctype.name != "void":
                with self.base_classes_path.open("r", encoding="utf-8") as f:
                    content = f.readlines()

                content.insert(
                    0,
                    f"from ctypes import  {typedef.ctype.py_string()}\n",
                )

                with self.base_classes_path.open("w", encoding="utf-8") as f:
                    f.writelines(content)

            with self.change_file(self.base_classes_path):
                super().print_typedef(typedef)
        elif isinstance(typedef.ctype, CtypesEnum):
            with self.change_file(self.enums_path):
                super().print_typedef(typedef)
        elif isinstance(typedef.ctype, CtypesFunction):
            with self.functions_path.open("r", encoding="utf-8") as f:
                content = f.readlines()

            for _module, _class in chain.from_iterable(
                self.module_from_type(ctype) for ctype in typedef.ctype.argtypes
            ):
                if _module.startswith(".."):
                    _module = f".{_module.lstrip('..')}"
                elif _module.startswith("."):
                    _module = f".structs.{_module.lstrip('.')}"

                content.insert(
                    0,
                    f"from {_module} import {_class}\n",
                )

            with self.functions_path.open("w", encoding="utf-8") as f:
                f.writelines(content)

            with self.change_file(self.functions_path):
                super().print_typedef(typedef)
        else:
            super().print_typedef(typedef)

    def print_enum(self, enum):
        with self.change_file(self.enums_path):
            super().print_enum(enum)

    def print_constant(self, constant):
        with self.change_file(self.constants_path):
            super().print_constant(constant)

    def srcinfo(self, src):
        return

    def _clean_type_str(self, type_str):
        """Removes redundant int() wrappers from array types for cleaner code."""
        # Replaces "BYTE * int(64)" with "BYTE * 64"
        return re.sub(r"\bint\((\d+)\)", r"\1", type_str)

    def print_simple_macro(self, macro):
        self.file.write(f"{macro.name} = {macro.expr.py_string(True)}")

    def print_loader(self):
        super().print_loader()
        self.file.write("\n\n")

        with EXTRA_FUNCTIONS_PATH.open() as f:
            self.file.write(f.read())

    def print_struct_members(self, struct):
        with self.struct_file(struct):
            if struct.opaque:
                return

            packed = False
            aligned = 1
            if struct.attrib.get("packed", False):
                aligned = struct.attrib.get("aligned", [1])
                assert len(aligned) == 1, (
                    "cgrammar gave more than one arg for aligned attribute"
                )
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

        arg_types_str = ", ".join(
            [self._clean_type_str(a.py_string()) for a in function.argtypes]
        )
        args_list = f"[{arg_types_str}]"

        restype_str = self._clean_type_str(function.restype.py_string())

        errcheck_str = "None"
        if function.errcheck:
            errcheck_str = function.errcheck.py_string()

        # Generate single line call to _F helper
        self.file.write(
            f"{function.py_name()} "
            f'= _F("{function.c_name()}", "{CC}", '
            f"{restype_str}, {args_list}, {errcheck_str})\n"
        )

    def print_variadic_function(self, function):
        CC = "stdcall" if function.attrib.get("stdcall", False) else "cdecl"

        arg_types_str = ", ".join(
            [self._clean_type_str(a.py_string()) for a in function.argtypes]
        )
        args_list = f"[{arg_types_str}]"

        restype_str = self._clean_type_str(function.restype.py_string())

        errcheck_str = "None"
        if function.errcheck:
            errcheck_str = function.errcheck.py_string()

        self.file.write(
            f"{function.py_name()} "
            f'= _FV("{function.c_name()}", "{CC}", '
            f"{restype_str}, {args_list}, {errcheck_str})\n"
        )

    def print_variable(self, variable):
        # Optional: Optimize variable loading too if needed.
        # For now, just standard try/except but cleaner is possible.
        # But variables are rare compared to functions in this SDK.
        super().print_variable(variable)
