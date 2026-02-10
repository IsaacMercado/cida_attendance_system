#!/usr/bin/env python3
"""Generate `src/cida_attendance/sdk/_generated.py` from `HCNetSDK.h` using ctypesgen.

- Headers: scripts/generate_sdk/incEn/
- Binaries: libs/ (default)

Uses CustomWrapperPrinter to:
- Avoid emitting srcinfo comments (file:line)
- Keep ctypesgen's cross-platform loader
- Load libraries guarded by try/except (missing names won't break import)
- Emit a portable runtime library search (dev/PyInstaller/Nuitka)
"""

import argparse
import importlib.util
import os
import sys
from pathlib import Path

from ctypesgen import main as ctypesgen_main
from ctypesgen import printer_python


def _load_custom_printer() -> type:
    here = Path(__file__).resolve().parent
    custom_printer_path = here / "custom_printer.py"
    spec = importlib.util.spec_from_file_location("custom_printer", custom_printer_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load: {custom_printer_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.CustomWrapperPrinter


def _libraries_for_platform() -> list[str]:
    """Return library names to probe via `-l`.

    Note: the custom printer wraps library loading in try/except, so we can
    list dependencies without breaking import on platforms where they don't
    exist.

    Current scope: Linux and Windows only.
    """

    if sys.platform.startswith("linux"):
        return [
            "libcrypto.so.1.1",
            "libssl.so.1.1",
            "libopenal.so.1",
            "libPlayCtrl.so",
            "libNPQos.so",
            "libAudioRender.so",
            "libSuperRender.so",
            "libHCCore.so",
            "libhpr.so",
            "libhcnetsdk.so",
        ]

    if sys.platform == "win32":
        return [
            "libcrypto-1_1-x64.dll",
            "libssl-1_1-x64.dll",
            "OpenAL32.dll",
            "zlib1.dll",
            "hlog.dll",
            "hpr.dll",
            "NPQos.dll",
            "AudioRender.dll",
            "SuperRender.dll",
            "PlayCtrl.dll",
            "HCCore.dll",
            "HCNetSDK.dll",
        ]

    raise RuntimeError(
        f"Unsupported platform for now: sys.platform={sys.platform!r}. "
        "Linux and Windows only."
    )


# Paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]
HEADERS_DIR = Path(__file__).parent / "incEn"
HEADER_FILE = HEADERS_DIR / "HCNetSDK.h"
OUTPUT_DIR = PROJECT_ROOT / "src" / "cida_attendance" / "sdk"
GENERATED_FILE = OUTPUT_DIR / "_generated.py"


def _resolve_libs_dir(libs_dir: str | None) -> Path:
    """Resolve the directory containing the native SDK binaries.

    Priority:
    1) CLI `--libs-dir`
    2) env `CIDA_ATTENDANCE_LIBS_DIR`
    3) repo default: `<project>/libs`
    """

    if libs_dir:
        return Path(libs_dir).expanduser().resolve()

    env_dir = os.environ.get("CIDA_ATTENDANCE_LIBS_DIR")
    if env_dir:
        return Path(env_dir).expanduser().resolve()

    return (PROJECT_ROOT / "libs").resolve()


def generate_full_sdk(*, libs_dir: Path) -> Path:
    """Generate the full SDK wrapper into `_generated.py`."""
    if not libs_dir.exists() or not libs_dir.is_dir():
        raise RuntimeError(f"libs_dir does not exist or is not a directory: {libs_dir}")

    # Fail fast if the libs directory doesn't match the current platform.
    if sys.platform == "win32":
        if not any(libs_dir.glob("*.dll")):
            raise RuntimeError(
                "No Windows DLLs were found in libs_dir. "
                f"Expected *.dll under: {libs_dir}"
            )
    elif sys.platform.startswith("linux"):
        if not (any(libs_dir.glob("*.so")) or any(libs_dir.glob("*.so.*"))):
            raise RuntimeError(
                "No Linux shared libraries were found in libs_dir. "
                f"Expected *.so / *.so.* under: {libs_dir}"
            )

    if not HEADER_FILE.exists():
        print(f"Header not found: {HEADER_FILE}")
        sys.exit(1)

    OUTPUT_DIR.mkdir(exist_ok=True)

    # Hook our custom printer (no separate runner).
    printer_python.WrapperPrinter = _load_custom_printer()

    # We list multiple names; the printer wraps loads in try/except.
    libs = _libraries_for_platform()
    argv = [
        str(HEADER_FILE),
        "-o",
        str(GENERATED_FILE),
        "-I",
        str(HEADERS_DIR),
        "--no-macro-warnings",
        "--allow-gnu-c",
    ]

    # ctypesgen tries to load libraries at *generation time* to detect the
    # source library for each symbol. On Windows, this requires explicit
    # library search dirs; otherwise you get warnings like:
    # "Could not load library \"X.dll\". Okay, I'll try to load it at runtime instead."
    #
    # `-L` adds directories for both compile-time and runtime in ctypesgen.
    # This is what prevents the "Could not load library ..." warnings.
    libdirs: list[Path] = [libs_dir]

    # Common vendor subdir (exists on both Windows and Linux SDKs).
    libdirs.append(libs_dir / "HCNetSDKCom")

    # Windows SDK often has extra DLLs in subfolders.
    if sys.platform == "win32":
        libdirs.append(libs_dir / "ClientDemoDll")

        # Ensure Windows can resolve *dependent* DLLs while ctypesgen attempts
        # to load libraries (it loads to detect each symbol's source library).
        # - Python 3.8+: prefer add_dll_directory
        # - Fallback: prepend to PATH
        dll_search_dirs = [str(d) for d in libdirs if d.is_dir()]
        add_dll_dir = getattr(os, "add_dll_directory", None)
        if callable(add_dll_dir):
            # Keep handles alive; otherwise the directory is removed again.
            _dll_dir_handles = []
            for d in dll_search_dirs:
                try:
                    _dll_dir_handles.append(add_dll_dir(d))
                except OSError:
                    pass
        else:
            old_path = os.environ.get("PATH", "")
            os.environ["PATH"] = ";".join(dll_search_dirs + [old_path])

    for d in libdirs:
        if d.is_dir():
            argv.extend(["-L", str(d)])

    for lib in libs:
        argv.extend(["-l", lib])

    try:
        ctypesgen_main.main(argv)
    except SystemExit as e:
        # ctypesgen calls sys.exit internally
        code = int(getattr(e, "code", 1) or 0)
        if code != 0:
            raise

    size_mb = GENERATED_FILE.stat().st_size / (1024 * 1024)
    print(f"Generated: {GENERATED_FILE} ({size_mb:.1f} MB)")

    # Count functions
    with open(GENERATED_FILE, "r") as f:
        content = f.read()

    import re

    functions = re.findall(r"(NET_DVR_\w+)\s*=", content)
    print(f"Functions: {len(functions):,}")

    return GENERATED_FILE


def main():
    parser = argparse.ArgumentParser(
        description="Generate src/cida_attendance/sdk/_generated.py from HCNetSDK.h"
    )
    parser.add_argument(
        "--libs-dir",
        default=None,
        help=(
            "Directory containing the native SDK binaries (DLLs/.so). "
            "Defaults to env CIDA_ATTENDANCE_LIBS_DIR or <project>/libs."
        ),
    )
    args = parser.parse_args()

    libs_dir = _resolve_libs_dir(args.libs_dir)
    generate_full_sdk(libs_dir=libs_dir)


if __name__ == "__main__":
    main()
