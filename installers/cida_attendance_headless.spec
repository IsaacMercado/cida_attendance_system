# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path

# Headless build (no GUI dependencies). Intended for Linux server deployments.
# Bundles `libs/` and the generated Hikvision wrapper.

SPEC_DIR = Path(SPECPATH)
ROOT_DIR = SPEC_DIR.parent

SRC_MAIN = str(ROOT_DIR / 'src' / 'cida_attendance' / '__main__.py')
LIBS_DIR = str(ROOT_DIR / 'libs')

a = Analysis(
    [SRC_MAIN],
    pathex=[],
    binaries=[],
    datas=[
        (LIBS_DIR, 'libs'),
    ],
    hiddenimports=[
        # Imported lazily via importlib in cida_attendance.sdk
        'cida_attendance.sdk._generated',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Explicitly exclude GUI stacks for a smaller, safer server build.
        'PySide6',
        'shiboken6',
        'tkinter',
        '_tkinter',
    ],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='cida_attendance',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='cida_attendance',
)
