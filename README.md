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

```pwsh
& "C:\Users\User\AppData\Local\Programs\Inno Setup 6\ISCC.exe" setup_script.iss
```
