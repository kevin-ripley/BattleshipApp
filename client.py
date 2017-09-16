import http.client as client
import sys
import re

#get command line arguments
str(sys.argv)
Address = sys.argv[1]
port = int(sys.argv[2])
X = int(sys.argv[3])
Y = int(sys.argv[4])

conn = client.HTTPConnection(Address, port)
conn.request("GET", "/board.txt")
response = client.HTTPResponse
r1 = conn.getresponse()
if(r1.status == 200):
    board = []
    body = str(r1.read())
    li = body.replace('b','')
    l = li.replace('\'','')
    list = l.replace('\\n', ' ')
    newlist = list.split(' ')
    board = newlist
    c = 5
    b = 4
    r = 3
    s = 3
    d = 2

    if (X > 10 or Y > 10):
        conn.send(b"HTTP NOT FOUND")
    if(board[X][Y] == 'C'):
        conn.send(b"HIT")
        c -= 1
        print("HIT Carrier, only", c, "left")
    if (board[X][Y] == 'B'):
        conn.send(b"HIT")
        b -= 1
        print("HIT Battleship, only", b, "left")
    if (board[X][Y] == 'R'):
        conn.send(b"HIT")
        r -= 1
        print("HIT Cruiser, only", r, "left")
    if (board[X][Y] == 'S'):
        conn.send(b"HIT")
        s -= 1
        print("HIT Submarine, only", s, "left")
    if (board[X][Y] == 'D'):
        conn.send(b"HIT")
        d -= 1
        print("HIT Destroyer, only", d, "left")


    else:
        conn.send(b"MISS")
        print("MISS")

