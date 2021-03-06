"""
Creates a simple TCP server

"""
import socket

# creates a server socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# gets the host
host = socket.gethostname()
# gets the port
port = 444

# binds the address and port to the socket
serversocket.bind((host, port))
# allows three connections to the socket
serversocket.listen(3)

while True:
    # Starting the connection
    clientsocket, address = serversocket.accept()
    print("Recieve connection from %s " % str(address))

    message = "Hello! Thank you for connecting to the server" + "\r\n"
    # sends an acknowledgment message to the client, must be encoded
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()