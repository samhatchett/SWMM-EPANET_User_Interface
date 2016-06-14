; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "SWMM-UI"
#define MyAppVersion "MTP 2"
#define MyAppPublisher "RESPEC"
#define MyAppURL "https://github.com/USEPA/SWMM-EPANET_User_Interface/"
#define MyAppExeName "frmMainSWMM.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{4A9E9EE4-89CF-4499-984C-953B386DEE7F}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
OutputDir=output
OutputBaseFilename=SWMM-UI-MTP2
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "swmmimages\*";         DestDir: "{app}\swmmimages"; Permissions: everyone-modify; Flags: ignoreversion recursesubdirs
Source: "dist\frmMainSWMM\*"; DestDir: "{app}"; Permissions: everyone-modify; Flags: ignoreversion recursesubdirs
Source: "C:\Users\Mark\Anaconda2\Library\plugins\sqldrivers\qsqlite4.dll"; DestDir: "{app}\plugins\sqldrivers"; Permissions: everyone-modify; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{userdesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

