# SendGrid Setup für Railway

## API Key als Environment Variable setzen

1. Gehen Sie zu Ihrem Railway Projekt Dashboard
2. Klicken Sie auf Ihr Service/Deployment
3. Gehen Sie zum Tab **"Variables"**
4. Klicken Sie auf **"New Variable"**
5. Fügen Sie hinzu:
   - **Name:** `SENDGRID_API_KEY`
   - **Value:** `[Ihr SendGrid API Key hier einfügen]`
6. Klicken Sie auf **"Add"**
7. Railway wird automatisch neu deployen

## Fertig!

Nach dem Deployment funktioniert die Email-Verifikation automatisch.

Die Emails werden von `noreply@brechersystem.ch` gesendet.

## Wichtig

- Der API Key ist nur als Environment Variable gesetzt
- Er ist NICHT im Code sichtbar
- Er wird NICHT in Git committed
- Nur Sie haben Zugriff darauf in Railway
