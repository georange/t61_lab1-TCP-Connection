# Import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket

# Figure out IP of hosting server	# sudo mn -x  	to start server
serverSocket.bind(("",9000)) 		# binds to all addresses in ifconfig 	#local loopback is 10.0.0.2
serverSocket.listen(1)          

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr =  serverSocket.accept() 
            
    try:
        message = connectionSocket.recv(10000)     
        filename = message.split()[1] 
        f = open(filename)
        outputdata = f.readlines()
                  
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n\n")

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):           
        	connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send("ERROR: file not found")

        # Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit() # Terminate the program after sending the corresponding data
