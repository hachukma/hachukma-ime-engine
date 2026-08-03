#define AppRoot "C:/Users/Anan Db/Desktop/Hachukma"
#define InstallerRoot "C:/Users/Anan Db/Desktop/Hachukma/installers"

[Setup]
AppId=F9FD119A-3E90-461C-BF01-2E312D3E8378
AppName=Hachukma
AppVersion=2.0
AppPublisher=Anan Debbarma
LicenseFile={#InstallerRoot}\EULA.text

DefaultDirName={autopf}\Hachukma
DefaultGroupName=Hachukma

OutputDir=..\installer_output
OutputBaseFilename=Hachukma-Installer

Compression=lzma2
SolidCompression=yes

PrivilegesRequired=lowest

WizardStyle=modern

UninstallDisplayIcon={app}\hachukma.ico


[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"


[Files]

; Main application
Source: "{#AppRoot}/dist/Hachukma IME.exe"; DestDir: "{app}"; Flags: ignoreversion

; Application icon
Source: "{#AppRoot}/assets/hachukma.ico"; DestDir: "{app}"; Flags: ignoreversion

; Font files
Source: "{#AppRoot}/font/Hachukma-Regular.ttf"; DestDir: "{app}/font"; Flags: ignoreversion

; License
Source: "{#InstallerRoot}\EULA.text"; DestDir: "{app}"; Flags: ignoreversion


[Icons]

; Start Menu shortcut
Name: "{group}\Hachukma IME"; Filename: "{app}\Hachukma IME.exe"; IconFilename: "{app}\hachukma.ico"

; Uninstall shortcut
Name: "{group}\Uninstall Hachukma IME"; Filename: "{uninstallexe}"

; Desktop shortcut
Name: "{autodesktop}\Hachukma IME"; Filename: "{app}\Hachukma IME.exe"; IconFilename: "{app}\hachukma.ico"


[Run]

Filename: "{app}\Hachukma IME.exe"; \
Description: "Launch Hachukma"; \
Flags: nowait postinstall skipifsilent
