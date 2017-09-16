import http.server
import socketserver
import sys

#This code parses command line arguments
#argument format: server.py <PORT#> <board.txt>
str(sys.argv)
PORT = sys.argv[1] #
board = sys.argv[2]


Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", int(PORT)), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
