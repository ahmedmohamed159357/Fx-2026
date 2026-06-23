; ─────────────────────────────────────────────────────────────────────────────
; TextFX v5  —  NSIS installer include (build/installer.nsh)
; Injected by electron-builder into the generated NSIS script.
; Windows 8.1 compatible — no SetRegView 64 requirement.
; ─────────────────────────────────────────────────────────────────────────────

; Write an uninstall entry so Add/Remove Programs works on Win 8.1
!macro customInstall
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\TextFX" \
      "DisplayName" "TextFX AI Creative Director"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\TextFX" \
      "UninstallString" "$INSTDIR\Uninstall TextFX.exe"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\TextFX" \
      "DisplayVersion" "5.0.0"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\TextFX" \
      "Publisher" "TextFX"
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\TextFX" \
      "NoModify" 1
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\TextFX" \
      "NoRepair" 1
!macroend

!macro customUninstall
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\TextFX"
  DeleteRegKey HKCU "Software\TextFX"
!macroend
