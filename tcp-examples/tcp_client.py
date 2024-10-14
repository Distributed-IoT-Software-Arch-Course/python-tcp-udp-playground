import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# Create a TCP/IP socket associated with the address family IPv4 and the socket type SOCK_STREAM
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # Connect to the server using the specified address and port
    s.connect((HOST, PORT))

    # Send a message to the server a buffer of 1024 bytes starting with the string "Hello, world"
    s.sendall(b'request=create_device;device_id=1;device_description=TestDevice')

    # Receive data from the server using a buffer of 1024 bytes
    data = s.recv(1024)

    # Close the connection
    s.close()

    # Print the received data
    print('Received', repr(data))

    str_message = data.decode("utf-8")
    request_array = str_message.split(";")

    for element in request_array:
        element_array = element.split("=")
        key = element_array[0]
        value = element_array[1]

        print(f'Received Key: {key} Value: {value}')