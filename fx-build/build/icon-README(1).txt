ICON PLACEHOLDER
────────────────
Place a 256×256 ICO file at:

    build/icon.ico

If you don't have one, generate it with ImageMagick:

    magick convert -size 256x256 xc:#1a1a2e -fill "#7c3aed" \
        -font Arial -pointsize 72 -gravity Center \
        -annotate 0 "FX" build/icon.ico

Or use any online ICO converter. The file MUST be a proper Windows ICO
(not just a renamed PNG) for NSIS and Windows 8.1 taskbar to render it.

electron-builder will fail gracefully with a default icon if icon.ico is
missing, but the installer will not have the branded icon.
