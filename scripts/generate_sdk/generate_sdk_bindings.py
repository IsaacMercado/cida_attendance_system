#!/usr/bin/env python3
"""Generate `src/cida_attendance/sdk/_generated.py` from `HCNetSDK.h` using ctypesgen.

- Headers: scripts/generate_sdk/incEn/
- Binaries: libs/

Uses CustomWrapperPrinter to:
- Avoid emitting srcinfo comments (file:line)
- Keep ctypesgen's cross-platform loader
- Load libraries guarded by try/except (missing names won't break import)
- Emit a portable runtime library search (dev/PyInstaller/Nuitka)
"""

import importlib.util
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
LIBS_DIR = PROJECT_ROOT / "libs"


def generate_full_sdk():
    """Generate the full SDK wrapper into `_generated.py`."""
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
        "--runtime-libdir",
        str(LIBS_DIR),
    ]

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
    generate_full_sdk()


if __name__ == "__main__":
    main()
