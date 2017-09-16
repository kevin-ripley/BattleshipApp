import http.client as client
import sys

#get command line arguments
str(sys.argv)
Address = sys.argv[1]
port = sys.argv[2]
X = sys.argv[3]
Y = sys.argv[4]

conn = client.HTTPConnection("localhost", port)
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)

