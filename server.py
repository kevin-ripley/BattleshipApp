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
location = {'00': 0, '01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0,
            '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0,
            '21': 0, '22': 0, '23': 0, '24': 0, '25': 0, '26': 0, '27': 0, '28': 0, '29': 0, '30': 0,
            '31': 0, '32': 0, '33': 0, '34': 0, '35': 0, '36': 0, '37': 0, '38': 0, '39': 0, '40': 0,
            '41': 0, '42': 0, '43': 0, '44': 0, '45': 0, '46': 0, '47': 0, '48': 0, '49': 0, '50': 0,
            '51': 0, '52': 0, '53': 0, '54': 0, '55': 0, '56': 0, '57': 0, '58': 0, '59': 0, '60': 0,
            '61': 0, '62': 0, '63': 0, '64': 0, '65': 0, '66': 0, '67': 0, '68': 0, '69': 0, '70': 0,
            '71': 0, '72': 0, '73': 0, '74': 0, '75': 0, '76': 0, '77': 0, '78': 0, '79': 0, '80': 0,
            '81': 0, '82': 0, '83': 0, '84': 0, '85': 0, '86': 0, '87': 0, '88': 0, '89': 0, '90': 0,
            '91': 0, '92': 0, '93': 0, '94': 0, '95': 0, '96': 0, '97': 0, '98': 0, '99': 0, '100': 0,}
newfile = 'board_count.pk'
locate = 'location.pk'

with open(newfile, 'wb') as file:
  pickle.dump(board_count, file)

with open(locate, 'wb') as file:
  pickle.dump(location, file)

class PostHandler(server.BaseHTTPRequestHandler):
    global b, c, d, r, s
    global coords
    def do_POST(self):

        with open(newfile, 'rb') as file:
            board_count = pickle.load(file)

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                'REQUEST_METHOD': 'POST',
                'CONTENT_TYPE': self.headers['Content-Type'],
            }
        )

        coords = []
        for field in form.keys():
            field_item = form[field]
            coords.append(form[field].value)

        with open(locate, 'rb') as file:
            loc = pickle.load(file)
        x = int(coords[0])
        y = int(coords[1])

        coord = ''.join(str(i) for i in coords)
        update = loc.get(coord)

        if (x >= 10 or y >= 10):
            self.send_error(404, "HTTP Not Found")
        if(coord and update == 0):
            loc[coord] = 1
            with open(locate, 'wb') as file:
                pickle.dump(loc, file)
            if (board[x][y] == 'C'):
                self.send_response(200, "hit=1")
                c = board_count.get('c')
                c -= 1
                board_count['c'] = c;
                with open(newfile, 'wb') as file:
                    pickle.dump(board_count, file)
                if (c == 0):
                    self.send_response(200, "hit=1&sunkC")
                    print("Carrier Sunk!")
                else:
                    self.send_response(200, "hit=1")
                    print("Carrier Hit!")
            if (board[x][y] == 'B'):
                self.send_response(200, "hit=1")
                b = board_count.get('b')
                b -= 1
                board_count['b'] = b;
                with open(newfile, 'wb') as file:
                    pickle.dump(board_count, file)
                if (b == 0):
                    self.send_response(200, "hit=1&sunkB")
                    print("Battleship Sunk!")
                else:
                    self.send_response(200, "hit=1")
                    print("Submarine Hit!")
            if (board[x][y] == 'R'):
                self.send_response(200, "hit=1")
                r = board_count.get('r')
                r -= 1
                board_count['r'] = r;
                with open(newfile, 'wb') as file:
                    pickle.dump(board_count, file)
                if (r == 0):
                    self.send_response(200, "hit=1&sunkR")
                    print("Cruiser Sunk!")
                else:
                    self.send_response(200, "hit=1")
                    print("Cruiser Hit!")

            if (board[x][y] == 'S'):
                s = board_count.get('s')
                s -= 1
                board_count['s'] = s;
                with open(newfile, 'wb') as file:
                    pickle.dump(board_count, file)
                if(s==0):
                    self.send_response(200, "hit=1&sunkS")
                    print("Submarine Sunk!")
                else:
                    self.send_response(200, "hit=1")
                    print("Submarine Hit!")
            if (board[x][y] == 'D'):
                d = board_count.get('d')
                d -= 1
                board_count['d'] = d;
                with open(newfile, 'wb') as file:
                    pickle.dump(board_count, file)
                if(d==0):
                    self.send_response(200, "hit=1&sunk=D")
                    print("hit=1&sunk=D")
                else:
                    self.send_response(200, "hit=1")
                    print("Destroyer Hit!")
            else:
                self.send_response(200, "hit=0")
                print("MISS, Try Again")

            self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
            self.end_headers()
        else:
            self.send_response(410, "Try a different coordinate")
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
