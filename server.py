import cgi
import http.server as server
import socketserver
import urllib.request
import urllib.parse as parse
import sys
from os import curdir, sep
import pickle


str(sys.argv)
port = sys.argv[1] #
global board
board = sys.argv[2]

battlefield = open(board)
body = battlefield.read()
l = body.replace('\'', '')
newlist = l.split('\n')
board = newlist

board_count = {'b': 4, 'c': 5, 'd': 2, 'r': 3, 's': 3}

newfile = 'board_count.pk'

with open(newfile, 'wb') as file:
  pickle.dump(board_count, file)

class PostHandler(server.BaseHTTPRequestHandler):
    global b, c, d, r, s
    def do_POST(self):

        with open(newfile, 'rb') as file:
            board_count = pickle.load(file)
        board_list = board_count.items()
        print(board_list)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'REQUEST_METHOD': 'POST',
                'CONTENT_TYPE': self.headers['Content-Type'],
            }
        )

        global coords
        coords = []
        for field in form.keys():
            field_item = form[field]
            coords.append(form[field].value)

        x = int(coords[0])
        y = int(coords[1])

        if (x >= 10 or y >= 10):
            self.send_error(404, "HTTP Not Found")
        if (board[x][y] == 'C'):
            self.send_response(200, "hit=1")
            c = board_count.get('c')
            c -= 1
            board_count['c'] = c;
            with open(newfile, 'wb') as file:
                pickle.dump(board_count, file)
            print("hit=1", + c)
        if (board[x][y] == 'B'):
            self.send_response(200, "hit=1")
            b = board_count.get('b')
            b -= 1
            board_count['b'] = b;
            with open(newfile, 'wb') as file:
                pickle.dump(board_count, file)
            print("Hit! with ", b, "hits")
        if (board[x][y] == 'R'):
            self.send_response(200, "hit=1")
            r = board_count.get('r')
            r -= 1
            board_count['r'] = r;
            with open(newfile, 'wb') as file:
                pickle.dump(board_count, file)
            print("hit=1")
        if (board[x][y] == 'S'):
            self.send_response(200, "hit=1")
            s = board_count.get('s')
            s -= 1
            board_count['s'] = s;
            with open(newfile, 'wb') as file:
                pickle.dump(board_count, file)
            print("hit=1")
        if (board[x][y] == 'D'):
            d = board_count.get('d')
            print(d)
            d -= 1
            board_count['d'] = d;
            with open(newfile, 'wb') as file:
                pickle.dump(board_count, file)
            if(d==0):
                self.send_response(200, "hit=1&sunk=D")
                print("hit=1&sunk=D")
            else:
                self.send_response(200, "hit=1")
                print("hit=1")
        else:
            self.send_response(200, "hit=0")
            print("MISS")

        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()

        f = open(curdir + sep + self.path)
        self.send_response(200)
        self.send_header('Content-Type',
                             'text/plain; charset=utf-8')
        self.end_headers()
        data = f.read().encode()
        self.wfile.write(data)
        f.close()
        return

if __name__ == '__main__':
    Handler = server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", int(port)), PostHandler) as httpd:
        print("Starting server at port", port, "use <Ctrl-C> to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()
