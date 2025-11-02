# Heppi.Me

Kurzes, modernes Portfolio / Landingpage — statische HTML‑Seite mit einfachem, sauberem CSS.

## Kurzbeschreibung
Heppi.Me ist eine minimalistische Portfolio‑/Landingpage, gebaut mit reinem HTML und CSS. Fokus liegt auf klarer Typographie, sanften Farben und einer leicht erweiterbaren Struktur.

## Features
- Einfache, responsive Struktur (kein Build‑Tool erforderlich)  
- Variablenbasiertes Design (CSS :root) für schnelle Anpassungen  
- Sticky Header, Intro‑Card mit Hover‑Effekten  
- Optionaler Dark/Light Mode via Klassen (.dark-mode / .light-mode)

## Technologie
- HTML5
- CSS (style.css)

## Schnellstart (lokal)
1. Repo in VS Code öffnen.  
2. index.html direkt im Browser öffnen — oder:
3. Mit VS Code Live Server:
   - Extension installieren → Rechtsklick auf `index.html` → "Open with Live Server".
4. Einfacher HTTP‑Server (PowerShell / Python):
   ```powershell
   cd c:\Users\leopold\Documents\GitHub\webb
   python -m http.server 3000
   # Öffne http://localhost:3000
   ```

## Favicons (abgerundete Ecken)
Browser‑Favicons können nicht per CSS gerundet werden. Erzeuge ein gerundetes Bild vorab (ImageMagick empfohlen):

```powershell
# ImageMagick erforderlich
magick "assets/favicon.png" -alpha set -virtual-pixel transparent -resize 64x64 `
  ( -size 64x64 xc:none -fill white -draw "roundrectangle 0,0,63,63,10,10" ) -compose DstIn -composite "assets/favicon_rounded.png"

magick "assets/favicon_rounded.png" -define icon:auto-resize=64,48,32,16 "assets/favicon.ico"
```

Im HTML dann verweisen:
```html
<link rel="icon" href="assets/favicon_rounded.png" type="image/png">
```

## Projektstruktur (relevant)
- index.html — Einstiegspunkt  
- style.css — alle Styles (zentrale Datei)  
- assets/ — Favicons, Bilder

Empfohlen (optional): Styles in mehrere Dateien aufteilen (variables, base, components, utils).

## Weiteres / To‑Do
- Accessibility prüfen (Kontrast, Semantik, ARIA)  
- Mehrere Favicon‑Größen bereitstellen  
- Optional: Build‑Pipeline (PostCSS/Autoprefixer) für bessere Browserunterstützung

## Mitwirken
Änderungen per Commit/PR. Kurzbeschreibung in Commit‑Message angeben.

## Lizenz
Keine Lizenz definiert. Bei Bedarf LICENSE (z. B. MIT) hinzufügen.

## Kontakt
Projektordner: c:\Users\leopold\Documents\GitHub\webb