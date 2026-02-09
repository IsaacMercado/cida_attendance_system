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

2. **Generate Installer (Inno Setup - Windows)**
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

```pwsh
python -m PyInstaller --name cida_attendance --windowed --distpath cida_attendance.dist --workpath cida_attendance.build --icon cida_attendance\assets\cida-logo.ico --add-data "cida_attendance\assets;cida_attendance\assets" --add-data "libs;libs" cida_attendance\__main__.py
```
