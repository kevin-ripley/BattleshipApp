import http.server
import socketserver
import sys
import ipaddress as ip

#This code parses command line arguments
#argument format: server.py <PORT#> <board.txt>
str(sys.argv)
port = sys.argv[1] #
board = sys.argv[2]


Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", int(port)), Handler) as httpd:
    print("Serving HTTP at port ", port)

    httpd.serve_forever()
