# Nuitka Build Guide  

This guide explains how to compile `cida-attendance` using Nuitka for optimized runtime performance.

## ⚡ Performance Note

The `cida_attendance.sdk._generated.py` file is **124,158 lines** of ctypes definitions. Nuitka compilation takes 10-20 minutes on first build, 5-10 minutes on subsequent builds (thanks to ccache).

**There is no way to skip heavy optimization of this file in Nuitka 2.6.6** - it must fully compile the C code. This is simply the trade-off for better runtime performance. Subsequent builds are faster due to caching.

## 📦 Standalone vs Onefile

**This project uses `--standalone` mode (NOT `--onefile`)** for important reasons:

### Why NOT onefile:
- ❌ **Windows antivirus blocks it** (false positive detection)
- ❌ **Native DLL loading issues** (Hikvision SDK libs may fail)
- ❌ **Slower startup** (must extract to temp every run)
- ❌ **Debugging harder** (everything in temp directory)

### Why standalone:
- ✅ **Antivirus friendly** (normal folder structure)
- ✅ **DLLs work correctly** (libs/ folder is accessible)
- ✅ **Faster execution** (no extraction overhead)
- ✅ **Easier debugging** (files visible in filesystem)
- ✅ **Professional distribution** (can be properly installed)

The output is a directory with all files. You can zip it or create an installer with Inno Setup.

## 📋 Prerequisites

### System Dependencies (Linux)

```bash
# Ubuntu/Debian
sudo apt-get install patchelf ccache

# Fedora/RHEL  
sudo dnf install patchelf ccache

# Arch Linux
sudo pacman -S patchelf ccache
```

### Python Dependencies

All dependencies are in `pyproject.toml`:
```bash
uv sync --dev
```

## 🚀 Build Commands

### Headless Build (No GUI - For Servers)

**Linux:**
```bash
uv run python -m nuitka \
    --standalone \
    --lto=yes \
    --output-dir=dist_nuitka \
    --include-data-dir=libs=libs \
    --nofollow-import-to=PySide6 \
    --nofollow-import-to=shiboken6 \
    --nofollow-import-to=tkinter \
    --show-progress \
    --show-memory \
    src/cida_attendance/__main__.py
```

**Windows:**
```powershell
uv run python -m nuitka `
    --standalone `
    --lto=yes `
    --output-dir=dist_nuitka `
    --include-data-dir=libs=libs `
    --nofollow-import-to=PySide6 `
    --nofollow-import-to=shiboken6 `
    --nofollow-import-to=tkinter `
    --show-progress `
    --show-memory `
    src\cida_attendance\__main__.py
```

**Output**: `dist_nuitka/__main__.dist/` directory with executable and all dependencies.

**Estimated time**: 10-20 minutes (first build), 5-10 minutes (subsequent)

### GUI Build (For Desktop Applications)

**Linux:**
```bash
uv run python -m nuitka \
    --standalone \
    --lto=yes \
    --enable-plugin=pyside6 \
    --output-dir=dist_nuitka \
    --include-data-dir=libs=libs \
    --include-data-dir=src/cida_attendance/ui/assets=cida_attendance/ui/assets \
    --show-progress \
    --show-memory \
    src/cida_attendance/__main__.py
```

**Windows:**
```powershell
uv run python -m nuitka `
    --standalone `
    --lto=yes `
    --enable-plugin=pyside6 `
    --windows-console-mode=disable `
    --windows-icon-from-ico=src\cida_attendance\ui\assets\cida-logo.ico `
    --output-dir=dist_nuitka `
    --include-data-dir=libs=libs `
    --include-data-dir=src\cida_attendance\ui\assets=cida_attendance\ui\assets `
    --show-progress `
    --show-memory `
    src\cida_attendance\__main__.py
```

**Output**: `dist_nuitka/__main__.dist/` directory.

**Estimated time**: 15-25 minutes (first build)

## ✅ Verifying the Build

After building, verify that libraries are properly included:

**Check libs directory:**
```bash
# Linux
ls -la dist_nuitka/__main__.dist/libs/
# Should show: libssl.so.1.1, libcrypto.so.1.1, libopenal.so.1, HCNetSDKCom/

# Windows
dir dist_nuitka\__main__.dist\libs\
# Should show DLL files and HCNetSDKCom folder
```

**Test the executable:**
```bash
# Linux
cd dist_nuitka/__main__.dist/
./__main__ --help

# Windows
cd dist_nuitka\__main__.dist\
__main__.exe --help
```

If libs are missing, the program will fail with "Failed to load Hikvision SDK libraries". If you see the help message, the build succeeded.

## 📦 Distribution

The entire `__main__.dist/` directory is your application. To distribute:

**Option 1: Zip Archive**
```bash
# Linux
cd dist_nuitka
zip -r cida_attendance_linux_x64.zip __main__.dist/

# Windows (PowerShell)
cd dist_nuitka
Compress-Archive -Path __main__.dist -DestinationPath cida_attendance_windows_x64.zip
```

**Option 2: Create Installer**
- **Windows**: Use Inno Setup with `installers/setup_script.iss`
- **Linux**: Use the packaging scripts to create .deb/.rpm packages

**Option 3: Direct Deployment**
```bash
# Copy entire directory to target server
scp -r dist_nuitka/__main__.dist/ user@server:/opt/cida_attendance/
```

**Important**: 
- Keep the directory structure intact (libs/ must be next to executable)
- Don't rename `__main__.dist` - the executable expects this location
- Set execute permissions on Linux: `chmod +x __main__`

## 🎯 Output Structure

After building:

```
dist_nuitka/
├── __main__.build/          # Cached build files (keep for faster rebuilds)
└── __main__.dist/           # ✅ DISTRIBUTE THIS DIRECTORY
    ├── __main__             # Main executable (Linux) or __main__.exe (Windows)
    ├── libs/                # ✅ Hikvision SDK libraries (CRITICAL)
    │   ├── libssl.so.1.1
    │   ├── libcrypto.so.1.1
    │   ├── libopenal.so.1
    │   └── HCNetSDKCom/
    ├── cida_attendance/     # Bundled Python code (compiled to C)
    └── [other dependencies] # Python runtime, Qt libs (if GUI), etc.
```

## 🔧 Build Options Explained

- `--standalone`: Bundle all dependencies
- `--onefile`: Single executable file
- `--lto=yes`: Link Time Optimization (smaller, faster binary)
- `--show-progress`: Show compilation phases
- `--show-memory`: Monitor RAM usage
- `--nofollow-import-to=X`: Don't include package X (reduces size)
- `--include-data-dir=src=dest`: Bundle data files

### Optional Optimization Flags

For faster development builds (sacrifice optimization):

```bash
--no-lto                    # Skip LTO (faster compile, larger binary)
--no-prefer-source-code     # Default: compile all to C
```

## 🐛 Troubleshooting

### Slow compilation of _generated.py

**This is normal.** The file has 124K lines of ctypes code. Nuitka must compile it all to C.

**Solutions:**
1. **Wait it out**: First build is slow, subsequent builds use cache
2. **Use PyInstaller** for development: Much faster builds (2-5 min vs 15-20 min)
3. **Use ccache**: Already helps, but won't eliminate the initial C compilation time
4. **Keep `__main__.build/` directory**: Don't delete between builds

### Errors

**"patchelf not found"**
```bash
uv pip install patchelf
```

**"ccache not found"**
```bash
sudo apt-get install ccache
```

**"Module not found at runtime"**
- Make sure all data files are included with `--include-data-dir`
- Check that libs directory contains all necessary .so files

## 📊 Comparison: Nuitka vs PyInstaller

| Aspect | Nuitka | PyInstaller |
|--------|---------|-------------|
| Runtime Speed | ⚡ Much faster | 🐌 Slower |
| Build Time | 🐌 10-25 minutes | ⚡ 2-5 minutes |
| Binary Size | 📦 Similar | 📦 Similar |
| Compatibility | ⚠️ Needs tuning | ✅ Works out-of-box |
| Debugging | 🔧 Harder | ✅ Easier |
| Development | 🐌 Slow iteration | ⚡ Fast iteration |

**Recommendation:**
- **Development**: Use PyInstaller (fast feedback)
- **Production**: Use Nuitka (better performance)

## 📝 Tips for Faster Builds

1. **Keep build cache**: Never delete `__main__.build/` directory between builds
2. **Use ccache**: Install system ccache package
3. **Parallel builds**: Nuitka uses all CPU cores automatically
4. **Development mode**: Use `--no-lto` during development
5. **Clean builds**: Only do full clean rebuild when changing dependencies

## 📁 About nuitka-package.yaml

The `nuitka-package.yaml` file in the project root is kept minimal because **Nuitka 2.6.6 has limited package configuration support**. Most options must be passed via command-line arguments.

The file exists for:
- Future compatibility with Nuitka >= 2.7
- Documentation of intent
- Potential for package-specific configurations

In Nuitka 2.7+, you can use full YAML configuration instead of long command lines.

## 🔗 References  

- [Official Nuitka Documentation](https://nuitka.net/doc/user-manual.html)
- [Package Configuration](https://nuitka.net/user-documentation/nuitka-package-config.html)
- [Command Line Options](https://nuitka.net/doc/user-manual.html#command-line)
