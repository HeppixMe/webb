# Heppi.Me

Kurze Beschreibung
- Statische Portfolio-/Landingpage mit einfacher Struktur (HTML + CSS).
- Fokus: klare Typographie, sanfte Farben und responsive Layout.

Status
- Prototyp / statische Seite — keine Build-Tools nötig.

Technologien
- HTML5
- CSS (style.css)
- Optional: VS Code Live Server oder ein einfacher HTTP-Server zum lokalen Testen

Projektstruktur (wichtigste Dateien)
- index.html — Einstiegspunkt
- style.css — alle Styles (siehe c:\Users\leopold\Documents\GitHub\webb\style.css)
- assets/ — Favicons und Bilder

Schnellstart (lokal)
1. Repo öffnen in VS Code.
2. Direkt: index.html im Browser öffnen.
3. Oder mit Live Server (empfohlen):
   - VS Code: "Live Server" Extension installieren → Rechtsklick auf index.html → "Open with Live Server".
4. Oder mit Python (PowerShell):
   ```powershell
   cd c:\Users\leopold\Documents\GitHub\webb
   python -m http.server 3000
   # dann im Browser: http://localhost:3000
   ```

Favicon: abgerundete Ecken erzeugen
- Browser-Favicons können nicht per CSS gerundet werden — ersetze das Favicon-Bild durch eine vorgerundete PNG/ICO.
- Beispiel (PowerShell + ImageMagick installiert):
  ```powershell
  magick "assets/favicon.png" -alpha set -virtual-pixel transparent -resize 64x64 `
    ( -size 64x64 xc:none -fill white -draw "roundrectangle 0,0,63,63,10,10" ) -compose DstIn -composite "assets/favicon_rounded.png"

  magick "assets/favicon_rounded.png" -define icon:auto-resize=64,48,32,16 "assets/favicon.ico"
  ```
- Danach in index.html auf die neue Datei verweisen:
  ```html
  <link rel="icon" href="assets/favicon_rounded.png" type="image/png">
  ```

Design / Styles
- Variablen sind in :root definiert (Farben, Abstände, Border-Radius).
- Header sticky, animierte Intro-Card, Utility-Klassen (.container, .hidden).
- Dark-/Light-Mode über .dark-mode / .light-mode möglich.

Weiteres / To‑Do Vorschläge
- CSS in mehrere Dateien (variables, base, components, utils) aufteilen.
- Kleine Accessibility-Checks (Kontrast, ARIA für Navigation).
- Favicons in mehreren Größen bereitstellen.

Mitwirken
- Änderungen via Pull Request oder direktes Commit im Repo.
- Bitte kurze Beschreibung jeder Änderung in Commit-Message.

Lizenz
- Keine Lizenz angegeben — falls nötig, LICENSE-Datei hinzufügen (z.B. MIT).

Kontakt
- Projekt unter c:\Users\leopold\Documents\GitHub\webb — bei Fragen Änderungen direkt in VS Code vornehmen.