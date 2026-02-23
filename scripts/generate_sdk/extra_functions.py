import os
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Callable, TypeVar

if TYPE_CHECKING:
    from ctypes import _CData

R = TypeVar("R")


# --- Helper: Functions ---
# Reduces 6+ lines of setup per function to 1 line.
# Handles stdcall/cdecl, argtypes, restype, and error checking.
def _F(
    name: str,
    cc: str,
    res: R,
    args: list["_CData"],
    err=None,
) -> Callable[..., R] | None:
    if not _libs[lib_name].has(name, cc):
        return None
    func = _libs[lib_name].get(name, cc)
    func.argtypes = args
    func.restype = res
    # Handle strict String return types if needed (logic from ctypesgen)
    if res is String:
        if sizeof(c_int) == sizeof(c_void_p):
            func.restype = ReturnString
        else:
            func.errcheck = ReturnString
    if err:
        func.errcheck = err
    return func


# --- Helper: Variadic Functions ---
def _FV(
    name: str,
    cc: str,
    res: R,
    args: list["_CData"],
    err=None,
) -> Callable[..., R] | None:
    if not _libs[lib_name].has(name, cc):
        return None
    func = _libs[lib_name].get(name, cc)
    return _variadic_function(func, res, args, err)


def _cida_candidate_library_dirs():
    dirs = []
    env_dir = os.environ.get("CIDA_ATTENDANCE_LIBS_DIR")
    if env_dir:
        dirs.append(env_dir)

    nuitka_temp = os.environ.get("NUITKA_ONEFILE_TEMP_DIR")
    if nuitka_temp:
        dirs.append(os.path.join(nuitka_temp, "libs"))

    if hasattr(sys, "_MEIPASS"):
        dirs.append(os.path.join(sys._MEIPASS, "libs"))

    try:
        exe_dir = os.path.dirname(sys.executable)
        if exe_dir:
            dirs.append(os.path.join(exe_dir, "libs"))
            dirs.append(os.path.join(exe_dir, "_internal", "libs"))
    except Exception:
        pass

    try:
        here = Path(__file__).resolve().parent
        for parent in [here, *here.parents]:
            libs_dir = parent / "libs"
            if libs_dir.is_dir():
                dirs.append(str(libs_dir))
            internal_libs_dir = parent / "_internal" / "libs"
            if internal_libs_dir.is_dir():
                dirs.append(str(internal_libs_dir))
    except Exception:
        pass

    # Expand base dirs to include vendor subdirs when present.
    expanded = []
    for d in dirs:
        expanded.append(d)
        expanded.append(os.path.join(d, "HCNetSDKCom"))

    out = []
    seen = set()
    for d in expanded:
        if not d or d in seen:
            continue
        seen.add(d)
        if os.path.isdir(d):
            out.append(d)
    return out


add_library_search_dirs(_cida_candidate_library_dirs())

if sys.platform == "win32":
    lib_name = "HCNetSDK.dll"
elif sys.platform == "linux":
    lib_name = "libhcnetsdk.so"
else:
    raise OSError(f"Unsupported platform: {sys.platform}")

_libs[lib_name] = load_library(lib_name)
