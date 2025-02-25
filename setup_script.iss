; Script de Inno Setup para instalar tu aplicación Python
; Asegúrate de ajustar las rutas y nombres según tus necesidades

[Setup]
AppName=CIDA Attendance System
AppVersion=1.0
DefaultDirName={pf}\CIDA Attendance System
DefaultGroupName=CIDA Attendance System
OutputDir=.
OutputBaseFilename=CIDA_Attendance_System_Setup
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64
PrivilegesRequired=admin

; Configuración del icono del instalador
SetupIconFile=cida_attendance\assets\cida-logo.ico

; Evitar que el antivirus bloquee el instalador
;SignTool=signtool

[Files]
; Copia todos los archivos generados por PyInstaller (carpeta dist)
Source: "cida_attendance.dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

; Si tienes un archivo de configuración adicional o recursos, agrégalos aquí
; Source: "config\*"; DestDir: "{app}\config"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
; Crear un acceso directo en el menú de inicio
Name: "{group}\My Python App"; Filename: "{app}\cida_attendance.exe"

; Opcional: Crear un acceso directo en el escritorio
Name: "{commondesktop}\My Python App"; Filename: "{app}\cida_attendance.exe"

[Run]
; Ejecutar el programa después de la instalación (opcional)
Filename: "{app}\cida_attendance.exe"; Parameters: "--width-icon"; Description: "Launch My Python App"; Flags: nowait postinstall skipifsilent

[Registry]
; Agregar la aplicación al registro para que se ejecute al iniciar Windows
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "CIDAAttendanceSystem"; ValueData: """{app}\cida_attendance.exe"" --width-icon"; Flags: uninsdeletevalue

[Code]
// Código personalizado para verificar si el antivirus bloquea el archivo
function InitializeSetup(): Boolean;
begin
  // Aquí puedes agregar lógica adicional si es necesario
  Result := True;
end;

// Código para manejar la desinstalación limpia
procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);
begin
  if CurUninstallStep = usPostUninstall then
  begin
    // Eliminar cualquier archivo residual o carpeta vacía
    DelTree(ExpandConstant('{app}'), True, True, True);
  end;
end;