#!/usr/bin/env python3
import http.server
import socketserver
import os
import json
import urllib.request
import urllib.parse

PORT = int(os.environ.get('PORT', 8080))
DIRECTORY = "."

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
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            try:
                # Send email via Web3Forms
                email_data = {
                    'access_key': '3b390291-efa0-4a79-afef-421ac9e8295a',
                    'from_name': 'Brechersystem',
                    'subject': 'Brechersystem - E-Mail Bestätigung',
                    'email': data['to'],
                    'message': f"""Hallo {data['name']},

Dein Bestätigungscode lautet:

{data['code']}

Gib diesen Code auf der Website ein, um deine Bewerbung abzuschließen.

Der Code ist 10 Minuten gültig.

Viele Grüße
Das Brechersystem Team"""
                }

                req = urllib.request.Request(
                    'https://api.web3forms.com/submit',
                    data=json.dumps(email_data).encode('utf-8'),
                    headers={'Content-Type': 'application/json'}
                )

                with urllib.request.urlopen(req) as response:
                    result = json.loads(response.read().decode('utf-8'))

                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'success': True}).encode('utf-8'))

            except Exception as e:
                print(f"Error sending email: {e}")
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
