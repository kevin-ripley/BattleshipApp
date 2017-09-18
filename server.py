import cgi
import http.server as server
import socketserver
import urllib.parse as request
import io
import sys
import ipaddress as ip

#This code parses command line arguments
#argument format: server.py <PORT#> <board.txt>
str(sys.argv)
port = sys.argv[1] #
global board
board = sys.argv[2]

battlefield = open(board)

class PostHandler(server.BaseHTTPRequestHandler):

    def do_POST(self):

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'REQUEST_METHOD': 'POST',
                'CONTENT_TYPE': self.headers['Content-Type'],
            }
        )

        # Begin the response
        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()
        out = io.TextIOWrapper(
            self.wfile,
            encoding='utf-8',
            line_buffering=False,
            write_through=True,
        )
        global coords
        coords = []
        for field in form.keys():
            field_item = form[field]
            coords.append(form[field].value)

        x = coords[0]
        y = coords[1]
        print(x, y)

        body = battlefield.read()
        l = body.replace('\'', '')
        newlist = l.split('\n')
        board = newlist
        c = 5
        b = 4
        r = 3
        s = 3
        d = 2

        if (int(x) > 10 or int(y) > 10):
            server.BaseHTTPRequestHandler.wfile(b"HTTP NOT FOUND")
        if (board[x][y] == 'C'):
            server.BaseHTTPRequestHandler.wfile(b"hit=1")
            c -= 1
            print("hit=1")
        if (board[x][y] == 'B'):
            server.BaseHTTPRequestHandler.wfile(b"hit=1")
            b -= 1
            print("Hit! with ", b, "left")
        if (board[x][y] == 'R'):
            server.BaseHTTPRequestHandler.wfile(b"hit=1")
            r -= 1
            print("hit=1")
        if (board[x][y] == 'S'):
            server.BaseHTTPRequestHandler.wfile(b"hit=1")
            s -= 1
            print("hit=1")
        if (board[x][y] == 'D'):
            server.BaseHTTPRequestHandler.wfile(b"hit=1")
            d -= 1
            print("hit=1")
        else:
            server.BaseHTTPRequestHandler.wfile(b"MISS")
            print("MISS")
        out.detach()

if __name__ == '__main__':
    Handler = server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", int(port)), PostHandler) as httpd:
        print("Starting server at port", port, "use <Ctrl-C> to stop")

        httpd.serve_forever()