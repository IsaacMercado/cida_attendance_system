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

## Nuitka Builds (Optimized Performance)

Nuitka provides better runtime performance than PyInstaller by compiling Python to C code.

**Important**: We use `--standalone` mode (directory with all files) instead of `--onefile` because:
- ✅ Windows antivirus won't block it
- ✅ Faster startup (no temp extraction needed)
- ✅ Better compatibility overall

### Build Commands

#### Headless Build (No GUI - For Servers)

```bash
uv run python -m nuitka --standalone src/cida_attendance
```

Output: `cida_attendance.dist/` directory with executable and dependencies.

**Note**: The large `_generated.py` file (124K lines) takes 10-20 minutes to compile on first build.

#### GUI Build (For Desktop)

##### Linux:

```bash
CIDA_GUI_BUILD=1 uv run python -m nuitka --standalone src/cida_attendance
```

The Fedora Atomic distribution gives an error with the `libatomic` library; to compile it you can run:

```bash
LIBRARY_PATH="$PWD/build_support/libatomic:${LIBRARY_PATH:-}" `
uv run python -m nuitka `
   --standalone `
   --noinclude-dlls=libatomic.so* `
   src/cida_attendance
```

##### Windows (PowerShell):

```bash
$env:CIDA_GUI_BUILD='1'; uv run python -m nuitka --standalone src/cida_attendance
```

**Estimated time**: 15-25 minutes (first build with GUI)

### Distribution

The build creates a `cida_attendance.dist/` directory with all dependencies. To distribute:

```bash
# Zip the entire directory
zip -r cida_attendance_linux_x64.zip cida_attendance.dist/

# Or create installers (see installers/README.md)
```

**Important**: Distribute the entire `cida_attendance.dist/` folder, not just the executable. The libs/ directory must be present.

## Linux Headless Deployment (no GUI)

### Build

```bash
rm -rf build dist
uv run pyinstaller installers/cida_attendance_headless.spec
```

### Run (manual)

From inside `cida_attendance.dist/`:

```bash
./cida_attendance.bin check
./cida_attendance.bin server PT1H --wait 0.5
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