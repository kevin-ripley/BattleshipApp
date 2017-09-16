import http.server
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import sys
import ipaddress as ip

#This code parses command line arguments
#argument format: server.py <PORT#> <board.txt>
str(sys.argv)
port = sys.argv[1] #
board = sys.argv[2]

class ServerHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        returnMessage = b"Hello World"
        self.wfile.write(returnMessage, "utf8")

def runServer():
    server_address = ('localhost', 5000)
    httpd = HTTPServer(server_address, ServerHandler)
    print('server running on localhost port 5000')
    httpd.serve_forever()

runServer()