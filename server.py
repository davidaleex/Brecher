#!/usr/bin/env python3
import http.server
import socketserver
import os
import json
import urllib.request
import urllib.parse

PORT = int(os.environ.get('PORT', 8080))
DIRECTORY = "."

# SendGrid API Key (must be set as environment variable)
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY', '')

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        # Handle verification email endpoint
        if self.path == '/api/send-verification':
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))

                print(f"📧 Attempting to send verification email to {data['to']}")
                print(f"🔑 API Key present: {bool(SENDGRID_API_KEY)}")
                print(f"🔑 API Key length: {len(SENDGRID_API_KEY) if SENDGRID_API_KEY else 0}")

                if not SENDGRID_API_KEY:
                    raise Exception("SENDGRID_API_KEY environment variable not set!")

                # Send email via SendGrid
                email_data = {
                    "personalizations": [{
                        "to": [{"email": data['to']}],
                        "subject": "Brechersystem - E-Mail Bestätigung"
                    }],
                    "from": {
                        "email": "noreply@brechersystem.ch",
                        "name": "Brechersystem"
                    },
                    "content": [{
                        "type": "text/plain",
                        "value": f"""Hallo {data['name']},

Dein Bestätigungscode lautet:

{data['code']}

Gib diesen Code auf der Website ein, um deine Bewerbung abzuschließen.

Der Code ist 10 Minuten gültig.

Viele Grüße
Das Brechersystem Team"""
                    }]
                }

                req = urllib.request.Request(
                    'https://api.sendgrid.com/v3/mail/send',
                    data=json.dumps(email_data).encode('utf-8'),
                    headers={
                        'Authorization': f'Bearer {SENDGRID_API_KEY}',
                        'Content-Type': 'application/json'
                    }
                )

                try:
                    with urllib.request.urlopen(req) as response:
                        response_body = response.read().decode('utf-8')
                        print(f"✅ Verification email sent to {data['to']}")
                        print(f"📨 SendGrid response: {response.status}")
                except urllib.error.HTTPError as e:
                    error_body = e.read().decode('utf-8')
                    print(f"❌ SendGrid HTTP Error {e.code}: {error_body}")
                    raise Exception(f"SendGrid error: {e.code} - {error_body}")

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'success': True}).encode('utf-8'))

            except Exception as e:
                import traceback
                print(f"❌ Error sending email: {e}")
                print(f"🔍 Full traceback:")
                traceback.print_exc()

                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'success': False, 'error': str(e)}).encode('utf-8'))

        else:
            # Serve static files
            super().do_POST()

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🚀 Server running on port {PORT}")
        print(f"📁 Serving files from {os.path.abspath(DIRECTORY)}")
        httpd.serve_forever()
