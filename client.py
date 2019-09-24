# Import socket module
from socket import *
import sys # In order to terminate the program

s = socket(AF_INET,SOCK_STREAM)

# Take command line arguments
ip = sys.argv[1]
port = sys.argv[2]
path = sys.argv[3]

s.connect((ip,port)) # Connect
s.send("GET " + path + " HTTP/1.0\n\n") # Send request
data = s.recv(10000) # Get response
s.close()
