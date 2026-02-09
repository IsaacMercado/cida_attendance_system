# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path

# Calculate paths relative to the .spec file (located in installers/)
SPEC_DIR = Path(SPECPATH)
ROOT_DIR = SPEC_DIR.parent

# Input paths
SRC_MAIN = str(ROOT_DIR / 'src' / 'cida_attendance' / '__main__.py')
ASSETS_DIR = str(ROOT_DIR / 'src' / 'cida_attendance' / 'ui' / 'assets')
LIBS_DIR = str(ROOT_DIR / 'libs')
ICON_PATH = str(ROOT_DIR / 'src' / 'cida_attendance' / 'ui' / 'assets' / 'cida-logo.ico')

a = Analysis(
    [SRC_MAIN],
    pathex=[],
    binaries=[],
    datas=[
        (ASSETS_DIR, 'cida_attendance/ui/assets'), 
        (LIBS_DIR, 'libs')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
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
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=[ICON_PATH],
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
