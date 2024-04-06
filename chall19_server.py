def escape(inp):
    blacklisted = ["bdefgijklmnopstuvxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789./,<>_;:~!@#$%^&[]{}"]
    flag = r"1_7H1NK_U_C4N_8EC0M3_A_CTF_3XP3RT"
    for char in inp:
        if char in blacklisted:
            return 'Invalid input'
    return eval(eval(inp))

import http.server
import socketserver
from urllib.parse import urlparse, parse_qs, unquote
import json

PORT = 8000

class myHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            parsed_path = urlparse(self.path)
            query_params = parse_qs(parsed_path.query)
            giveninp = query_params['input'][0]
            escaped = escape(unquote(giveninp))
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            json_string = json.dumps({"message": escaped})
            self.wfile.write(json_string.encode())
        except:
            self.send_response(400)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            json_string = json.dumps({"message": "Invalid input"})
            self.wfile.write(json_string.encode())

handler = myHandler
httpd = socketserver.TCPServer(("", PORT), handler)
httpd.serve_forever()
        