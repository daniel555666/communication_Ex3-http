# import socket module
import socket
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
serverSocket.bind(('',3000))
serverSocket.listen(1)
# Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket,addr =serverSocket.accept()  # Fill in start              #Fill in end
    try:
        message =connectionSocket.recv(1024)  # Fill in start          #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata =f.read()  # Fill in start       #Fill in end
        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send(("HTTP/1.1 200 OK\r\n\r\n").encode("utf-8"))
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
# Send response message for file not found
# Fill in start
        connectionSocket.send(("HTTP/1.1 404 Not Found\r\n\r\n").encode("utf-8"))
        # connectionSocket.send(("<html><head><html><body>Hellow World</body></html>").encode())
# Fill in end
# Close client socket
# Fill in start
    connectionSocket.close()
# Fill in end
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
