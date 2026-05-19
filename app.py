from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "<h1>Hello from Docker!</h1><p>Version 2 - I understand layers!</p>"
        self.wfile.write(message.encode())
    
    def log_message(self, format, *args):
        print(f"Request: {args[0]} -> {args[1]}")

print("Server starting on port 8000...")
HTTPServer(('0.0.0.0', 8000), Handler).serve_forever()
