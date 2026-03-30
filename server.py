import http.server
import socketserver
import os

PORT = 5000
HOST = "0.0.0.0"

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "":
            self.path = "/modern-genset-panel-v3.html"
        return super().do_GET()

    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}")

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    print(f"Serving on http://{HOST}:{PORT}")
    httpd.serve_forever()
