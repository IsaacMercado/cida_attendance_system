## Executable and Installer Generation

### New Method (Recommended)

1. **Generate Executable (PyInstaller)**
   Run from the project root:
   ```bash
   # Clean previous builds
   rm -rf build dist
   
   # Generate executable using the updated spec file
   uv run pyinstaller installers/cida_attendance.spec
   ```
   This will generate the `dist/cida_attendance` folder in the root.

   Notes:
   - The build relies on `installers/cida_attendance.spec` to bundle `libs/` and to include the generated Hikvision wrapper module (which is imported lazily at runtime).

2. **Generate Executable (PyInstaller, Headless/Linux server)**
   This build excludes GUI dependencies (smaller + fewer runtime deps).
   ```bash
   # Clean previous builds
   rm -rf build dist

   # Build headless bundle
   uv run pyinstaller installers/cida_attendance_headless.spec
   ```
   Output: `dist/cida_attendance/`

3. **Generate Installer (Inno Setup - Windows)**
   This step requires Windows.
   1. Open `installers/setup_script.iss` with Inno Setup Compiler.
   2. Compile the script.
   3. The `.exe` installer will appear in the `installers/` folder.

   Alternatively via command line (Windows):
   ```pwsh
   & "C:\Users\User\AppData\Local\Programs\Inno Setup 6\ISCC.exe" installers\setup_script.iss
   ```

### Old Methods (Reference)

```bash
python -m nuitka `
  --standalone `
  --onefile `
  --windows-console-mode=attach `
  --enable-plugin=pyside6 `
  --include-data-dir=cida_attendance/assets=cida_attendance/assets `
  --include-data-dir=libs=libs `
  --output-dir=cida_attendance_nuitka.dist `
  --windows-icon-from-ico=cida_attendance/assets/cida-logo.ico `
  --output-filename=cida_attendance.exe `
  cida_attendance\__main__.py
```

## Nuitka Builds (Optimized Performance)

Nuitka provides better runtime performance than PyInstaller by compiling Python to C code.

**Important**: We use `--standalone` mode (directory with all files) instead of `--onefile` because:
- ✅ Windows antivirus won't block it
- ✅ Native DLLs (Hikvision SDK) work correctly
- ✅ Faster startup (no temp extraction needed)
- ✅ Better compatibility overall

### Build Commands

#### Headless Build (No GUI - For Servers)

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

Output: `dist_nuitka/__main__.dist/` directory with executable and dependencies.

**Note**: The large `_generated.py` file (124K lines) takes 10-20 minutes to compile on first build.

#### GUI Build (For Desktop)

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

**Estimated time**: 15-25 minutes (first build with GUI)

### Distribution

The build creates a `dist_nuitka/__main__.dist/` directory with all dependencies. To distribute:

```bash
# Zip the entire directory
cd dist_nuitka
zip -r cida_attendance_linux_x64.zip __main__.dist/

# Or create installers (see installers/README.md)
```

**Important**: Distribute the entire `__main__.dist/` folder, not just the executable. The libs/ directory must be present.

#### Windows-Specific Options

Add these flags for Windows builds:

```powershell
--windows-icon-from-ico=src\cida_attendance\ui\assets\cida-logo.ico
--windows-console-mode=disable  # For GUI builds only
```

See [NUITKA_BUILD.md](NUITKA_BUILD.md) for detailed documentation and optimization tips.

## Linux Headless Deployment (no GUI)

### Build

```bash
rm -rf build dist
uv run pyinstaller installers/cida_attendance_headless.spec
```

### Run (manual)

From inside `dist/cida_attendance/`:

```bash
./cida_attendance check
./cida_attendance server PT1H --wait 0.5
```

Environment overrides:

- `CONFIG_FILE=/path/to/config.json` (if you deploy configs outside the bundle)
- `CIDA_ATTENDANCE_LIBS_DIR=/path/to/libs` (only if you keep `libs/` external)

### Run as a service (systemd)

Example unit file (adjust paths/user):

```ini
[Unit]
Description=CIDA Attendance (Headless)
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=cida
Group=cida
WorkingDirectory=/opt/cida_attendance
ExecStart=/opt/cida_attendance/cida_attendance server PT1H --wait 0.5
Restart=always
RestartSec=2

# Optional overrides
# Environment=CONFIG_FILE=/etc/cida_attendance/config.json
# Environment=CIDA_ATTENDANCE_LIBS_DIR=/opt/cida_attendance/libs

[Install]
WantedBy=multi-user.target
```

## Secure Packaging & Distribution Notes

- Prefer the headless build for servers: smaller dependency surface.
- Run as a dedicated, unprivileged user (e.g. `cida`) and keep config files `0600`.
- Distribute releases with checksums (e.g. `sha256sum -b` on Linux) and verify on each site.
- Windows: sign the final installer/exe (Authenticode) to reduce SmartScreen prompts.
- Keep `libs/` and `HCNetSDKCom/` from the vendor SDK together; do not cherry-pick files unless you fully understand their dependency graph.

## Linux .deb / .rpm Packages

This repo includes a packaging flow that produces both `.deb` and `.rpm` using `nfpm`.

1. Install `nfpm` (pick one):
   - `go install github.com/goreleaser/nfpm/v2/cmd/nfpm@latest`
   - Or download a release binary from the nfpm GitHub releases.

2. Build packages:
   ```bash
   ./scripts/build_linux_packages.sh
   ```

Outputs:
- `dist/*.deb`
- `dist/*.rpm`

Notes:
- The packages install the headless bundle into `/opt/cida_attendance/` and a symlink at `/usr/bin/cida_attendance`.
- A systemd unit is installed at `/usr/lib/systemd/system/cida-attendance.service` but is NOT enabled automatically.

```bash
LD_LIBRARY_PATH=$PWD/libs python scripts/generate_sdk/generate_sdk_bindings.py
```