# EmailJS Setup für E-Mail-Verifikation

Die Website nutzt EmailJS für das Versenden von Verifikationscodes. Folgen Sie diesen Schritten:

## 1. EmailJS Account erstellen

1. Gehen Sie zu https://www.emailjs.com/
2. Registrieren Sie sich (kostenlos - 200 Emails pro Monat)
3. Bestätigen Sie Ihre E-Mail-Adresse

## 2. Email Service hinzufügen

1. Gehen Sie zu "Email Services" → "Add New Service"
2. Wählen Sie Ihren E-Mail-Provider (z.B. Gmail, Outlook, etc.)
3. Folgen Sie den Anweisungen zum Verbinden Ihres E-Mail-Kontos
4. Notieren Sie die **Service ID**

## 3. Email Template erstellen

1. Gehen Sie zu "Email Templates" → "Create New Template"
2. Template Name: "Brechersystem Verification"
3. Verwenden Sie folgende Template-Variablen:

```
Hallo {{to_name}},

Dein Bestätigungscode für die Brechersystem-Bewerbung lautet:

{{verification_code}}

Gib diesen Code auf der Website ein, um deine Bewerbung abzuschließen.

Der Code ist 10 Minuten gültig.

Viele Grüße
Das Brechersystem Team
```

4. Subject: `Dein Brechersystem Bestätigungscode`
5. To Email: `{{to_email}}`
6. Speichern und notieren Sie die **Template ID**

## 4. Public Key finden

1. Gehen Sie zu "Account" → "General"
2. Kopieren Sie Ihren **Public Key**

## 5. Keys in index.html eintragen

Öffnen Sie `index.html` und ersetzen Sie folgende Zeilen:

```javascript
// Zeile ~1501
emailjs.init("YOUR_PUBLIC_KEY");  // ← Hier Ihren Public Key eintragen

// Zeile ~1541
await emailjs.send('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', templateParams);
//                  ↑ Service ID       ↑ Template ID
```

### Beispiel:
```javascript
emailjs.init("AbCdEfGhIjKlMnOp");
await emailjs.send('service_abc123', 'template_xyz789', templateParams);
```

## 6. Testen

1. Speichern Sie die Datei
2. Pushen Sie die Änderungen
3. Testen Sie das Formular auf Ihrer Live-Website

## Wichtig

- Die EmailJS Free-Version erlaubt 200 Emails pro Monat
- Alle Emails werden von Ihrem verbundenen E-Mail-Konto gesendet
- Die Keys sind öffentlich sichtbar (das ist bei EmailJS normal und sicher)

## Support

Bei Problemen: https://www.emailjs.com/docs/
