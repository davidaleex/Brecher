# BRECHER Coaching Website

Moderne Onepager-Website für BRECHER Coaching mit Kontaktformular.

## Features
- 🎨 Waldgrünes Design mit weißer Schrift
- 📱 Vollständig responsive
- ✨ Animierte Hintergrund-Partikel und Hover-Effekte
- 📧 Kontaktformular mit E-Mail-Benachrichtigung
- 🚀 Optimiert für Vercel

## Setup Kontaktformular

Das Kontaktformular nutzt **Web3Forms** (kostenlos):

1. Gehe zu [https://web3forms.com](https://web3forms.com)
2. Klicke auf "Get Started for Free"
3. Gib deine E-Mail-Adresse ein (an die die Formulare gesendet werden)
4. Du erhältst einen **Access Key** per E-Mail
5. Öffne `index.html` und ersetze `YOUR_ACCESS_KEY_HERE` mit deinem Key:
   ```html
   <input type="hidden" name="access_key" value="DEIN_ACCESS_KEY_HIER">
   ```

## Deployment auf Vercel

### Variante 1: Mit Vercel CLI
```bash
# Vercel CLI installieren
npm i -g vercel

# Im Projekt-Ordner deployen
vercel
```

### Variante 2: Mit GitHub (empfohlen)
1. Code ist bereits auf GitHub gepusht
2. Gehe zu [https://vercel.com](https://vercel.com)
3. Klicke "Import Project"
4. Verbinde dein GitHub Repository: `davidaleex/Brecher`
5. Klicke "Deploy"

Fertig! Deine Website ist live.

## Custom Domain (brecher.ch) verbinden

1. In Vercel Dashboard → Settings → Domains
2. Domain hinzufügen: `brecher.ch` und `www.brecher.ch`
3. DNS-Einträge bei deinem Domain-Provider aktualisieren:
   ```
   A Record:   @ → 76.76.21.21
   CNAME:      www → cname.vercel-dns.com
   ```

## Lokale Entwicklung

Einfach `index.html` im Browser öffnen - kein Server nötig!

---

🤖 Created with [Claude Code](https://claude.com/claude-code)
