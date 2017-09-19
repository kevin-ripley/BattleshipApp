import http.client as client
import urllib.parse
import urllib.request
import sys
import re

#get command line arguments
Address = sys.argv[1]
port = sys.argv[2]
X = sys.argv[3]
Y = sys.argv[4]

params = urllib.parse.urlencode({'x':X, 'y':Y})
headers = {"Content-type":"application/x-www-form-urlencoded", "Accept":"text/plain"}
conn = client.HTTPConnection(Address, port)

conn.request("POST", "/", params, headers)
response = conn.getresponse()
print(response.status, response.reason)

