import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

# Create a TCP/IP socket associated with the address family IPv4 and the socket type SOCK_STREAM
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Bind the socket to the address and port
    s.bind((HOST, PORT))

    # Enable the server to accept connections
    s.listen()

    # Print a message to indicate that the server is waiting for incoming client connections
    print("Waiting for incoming client connections ...")

    # Accept a connection from a client
    conn, addr = s.accept()

    # With the connection established communicate with the client
    with conn:
        print('Connected by', addr)
        while True:
            # Receive data from the client using a buffer of 1024 bytes
            data = conn.recv(1024)
            print("Received Message: {}".format(data))
            if not data:
                break
            # Send the received data back to the client (acting as an echo server)
            conn.sendall(data)