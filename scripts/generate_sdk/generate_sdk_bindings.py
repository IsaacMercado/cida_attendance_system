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

    argv = [
        str(HEADER_FILE),
        "-o",
        str(GENERATED_FILE),
        "-I",
        str(HEADERS_DIR),
        "--no-macro-warnings",
        "--allow-gnu-c",
        # "--no-embed-preamble"
    ]

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
