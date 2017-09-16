import http.client as client
import sys

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
body = response.read(r1, 256)
print(r1.status, r1.reason, body)

