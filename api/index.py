from http.server import BaseHTTPRequestHandler
import subprocess


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        process = subprocess.run(["ffmpeg"]) 
        result = process.stdout.decode('utf-8')
        self.send_response(200, result)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return
