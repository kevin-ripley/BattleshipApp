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

        x = int(coords[0])
        y = int(coords[1])
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



        if (x > 10 or y > 10):
            self.send_response(404, "HTTP Not Found")
        if (board[x][y] == 'C'):
            self.send_response(200, "hit=1")
            c -= 1
            print("hit=1")
        if (board[x][y] == 'B'):
            self.send_response(200, "hit=1")
            b -= 1
            print("Hit! with ", b, "left")
        if (board[x][y] == 'R'):
            self.send_response(200, "hit=1")
            r -= 1
            print("hit=1")
        if (board[x][y] == 'S'):
            self.send_response(200, "hit=1")
            s -= 1
            print("hit=1")
        if (board[x][y] == 'D'):
            self.send_response(200, "hit=1")
            d -= 1
            print("hit=1")
        else:
            self.send_response(200, "hit=0")
            print("MISS")

        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()
        out.detach()

if __name__ == '__main__':
    Handler = server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", int(port)), PostHandler) as httpd:
        print("Starting server at port", port, "use <Ctrl-C> to stop")

        httpd.serve_forever()