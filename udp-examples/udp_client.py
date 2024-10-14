import socket

msgFromClient = "request=create_device;device_id=1;device_description=TestDevice"
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Message from Server {}".format(msgFromServer[0])

str_message = msgFromServer[0].decode("utf-8")
request_array = str_message.split(";")

for element in request_array:

    element_array = element.split("=")
    key = element_array[0]
    value = element_array[1]

    print(f'Received Key: {key} Value: {value}')