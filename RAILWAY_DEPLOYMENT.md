# Railway Deployment für brechersystem.ch

## 🚀 Deployment Schritte

### 1. Railway Projekt erstellen

1. Gehe zu **https://railway.app**
2. Klicke "Start a New Project"
3. Wähle "Deploy from GitHub repo"
4. Verbinde dein GitHub und wähle: `davidaleex/Brecher`
5. Railway deployed automatisch!

### 2. Domain verbinden

#### In Railway:
1. Gehe zu deinem Projekt
2. Klicke auf "Settings" → "Domains"
3. Klicke "Custom Domain"
4. Gib ein: `brechersystem.ch`
5. Railway zeigt dir die DNS-Einträge

#### Bei deinem Domain-Provider (z.B. Hostpoint, Infomaniak):
1. Gehe zu DNS-Einstellungen
2. Füge folgende Einträge hinzu:

**Für Hauptdomain (brechersystem.ch):**
```
Type: CNAME
Name: @
Value: [railway-url].railway.app
```

**Für www (www.brechersystem.ch):**
```
Type: CNAME
Name: www
Value: [railway-url].railway.app
```

> Railway zeigt dir die genauen Werte im Dashboard!

### 3. Warten

- DNS-Propagation dauert 5 Minuten - 24 Stunden
- SSL-Zertifikat wird automatisch erstellt
- Railway zeigt "Active" wenn fertig

## 🔧 Lokaler Test

```bash
python server.py
# Öffne: http://localhost:8080
```

## 📝 Environment Variables

Keine nötig für die statische Website!

Später für Kontaktformular:
- `WEB3FORMS_ACCESS_KEY` → Dein Web3Forms Key

## 💰 Kosten

- **Hobby Plan:** $5/Monat
- **Pro Plan:** $20/Monat (mit $5 Free Credits zum Start)

## 🔄 Updates deployen

```bash
git add .
git commit -m "Update website"
git push
```

Railway deployed automatisch nach jedem Push!

## 🐛 Troubleshooting

### Deployment schlägt fehl?
- Check Railway Logs im Dashboard
- `railway.json` korrekt?
- `server.py` vorhanden?

### Domain funktioniert nicht?
- DNS-Einträge korrekt?
- 24h gewartet?
- Check mit: `dig brechersystem.ch`

### SSL-Zertifikat fehlt?
- Warte 10-15 Minuten nach DNS-Setup
- Railway erstellt es automatisch

## 📞 Support

Railway Discord: https://discord.gg/railway
Docs: https://docs.railway.app

---

🤖 Created with [Claude Code](https://claude.com/claude-code)
