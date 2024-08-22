# server.py
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

PORT = int(os.getenv('PORT', 8080))

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

with HTTPServer(('', PORT), CustomHTTPRequestHandler) as server:
    print(f"Serving on port {PORT}")
    server.serve_forever()
