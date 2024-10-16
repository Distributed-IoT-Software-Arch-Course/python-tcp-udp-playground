import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024
msgFromServer = "response=OK;msg=device_created"
bytesToSend = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams
while (True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)

    str_message = message.decode("utf-8")
    request_array = str_message.split(";")

    for element in request_array:

        element_array = element.split("=")
        key = element_array[0]
        value = element_array[1]

        print(f'Received Key: {key} Value: {value}')

    print(clientMsg)
    print(clientIP)

    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)