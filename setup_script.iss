; Script de Inno Setup para instalar tu aplicación Python
; Asegúrate de ajustar las rutas y nombres según tus necesidades

[Setup]
AppName=CIDA Attendance System
AppVersion=1.0
DefaultDirName={autopf}\CIDA Attendance System
DefaultGroupName=CIDA Attendance System
OutputDir=.
OutputBaseFilename=CIDA_Attendance_System_Setup
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64compatible
PrivilegesRequired=admin

; Configuración del icono del instalador
SetupIconFile=cida_attendance\assets\cida-logo.ico

; Evitar que el antivirus bloquee el instalador
;SignTool=signtool

[Files]
; Copia todos los archivos generados por PyInstaller (build one-dir)
; La carpeta resultante será cida_attendance.dist\cida_attendance\*
Source: "cida_attendance.dist\cida_attendance\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; Si decides usar --onefile y mover libs externamente, agrega entradas separadas.

; Si tienes un archivo de configuración adicional o recursos, agrégalos aquí
; Source: "config\*"; DestDir: "{app}\config"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
; Acceso directo para iniciar en modo GUI con icono
Name: "{group}\CIDA Attendance System"; Filename: "{app}\cida_attendance.exe"; Parameters: "server --with-icon"; WorkingDir: "{app}"
Name: "{commondesktop}\CIDA Attendance System"; Filename: "{app}\cida_attendance.exe"; Parameters: "server --with-icon"; WorkingDir: "{app}"

[Run]
; Ejecutar después de instalar (opcional). Usa GUI por defecto.
Filename: "{app}\cida_attendance.exe"; Parameters: "server --with-icon"; Description: "Iniciar CIDA Attendance"; Flags: nowait postinstall skipifsilent

[Registry]
; Inicio automático (opcional). Comenta si no lo deseas.
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "CIDAAttendanceSystem"; ValueData: """{app}\cida_attendance.exe"" server --with-icon"; Flags: uninsdeletevalue

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