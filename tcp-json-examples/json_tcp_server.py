import socket
import json
from json import JSONDecodeError
from service_message import ServiceMessage

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# Create a TCP/IP socket associated with the address family IPv4 and the socket type SOCK_STREAM
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Bind the socket to the address and port
    s.bind((HOST, PORT))

    # Enable the server to accept connections
    s.listen()

    print("Waiting for incoming client connections ...")

    # Accept a connection from a client
    conn, addr = s.accept()

    # With the connection established communicate with the client
    with conn:
        print('Connected by', addr)
        while True:

            # Receive data from the client using a buffer of 1024 bytes
            data = conn.recv(1024)

            # Decode the received data to a string using the decode method
            receivedString = data.decode('UTF-8')

            # Check if the received data is not empty
            if len(data) > 0:
                try:
                    # Parse the received JSON string to a Python dictionary using the json.loads method
                    print("Received Message: {}".format(receivedString))
                    serviceMessage = ServiceMessage(**json.loads(receivedString))
                    print(serviceMessage)
                    # Send an OK response to the client
                    conn.sendall(str.encode("OK"))
                except JSONDecodeError:
                    print("Error parsing received command !")
                    # Send a KO response to the client
                    conn.sendall(str.encode("KO"))
            if not data:
                # Break the loop if no data is received and send a KO response to the client
                conn.sendall(str.encode("KO"))
                break
