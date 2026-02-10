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

## Windows Packaging (Nuitka)

This project uses a generated ctypes wrapper for Hikvision (HCNetSDK). The runtime expects `libs/` to be present either:

- Next to the executable (standalone builds)
- Under the extracted onefile directory (onefile builds)

The loader supports:

- `CIDA_ATTENDANCE_LIBS_DIR` override
- Nuitka onefile temp dir layout: `%NUITKA_ONEFILE_TEMP_DIR%\libs`

### GUI build (tray icon / optional GUI commands)

PowerShell example (run from repo root):

```pwsh
uv run python -m nuitka `
   --standalone `
   --onefile `
   --enable-plugin=pyside6 `
   --windows-console-mode=disable `
   --follow-imports `
   --include-module=cida_attendance.sdk._generated `
   --include-data-dir=src\cida_attendance\ui\assets=cida_attendance\ui\assets `
   --include-data-dir=libs=libs `
   --output-dir=dist_nuitka `
   --windows-icon-from-ico=src\cida_attendance\ui\assets\cida-logo.ico `
   --output-filename=cida_attendance.exe `
   src\cida_attendance\__main__.py
```

### CLI-only build (recommended for admin tools)

```pwsh
uv run python -m nuitka `
   --standalone `
   --onefile `
   --windows-console-mode=attach `
   --follow-imports `
   --include-module=cida_attendance.sdk._generated `
   --include-data-dir=libs=libs `
   --output-dir=dist_nuitka `
   --output-filename=cida_attendance.exe `
   src\cida_attendance\__main__.py
```

### Linux Nuitka notes

Nuitka on Linux typically requires extra system tooling/libraries (e.g. `patchelf`, and on some distros `libatomic-static` / Python development packages). If you're using `uv`, you can usually satisfy `patchelf` with `uv pip install patchelf`.

In this repo we currently recommend PyInstaller for Linux deployments, and keep Nuitka primarily for Windows performance builds.

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
