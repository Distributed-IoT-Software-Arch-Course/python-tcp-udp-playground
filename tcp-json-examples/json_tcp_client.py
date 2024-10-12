import socket
from iot_device import IoTDevice
from service_message import ServiceMessage

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# Create a new IoT Device instance
iotDevice = IoTDevice("device-0001", "acme-inc", "v0.0.1-beta", 44.101010, 10.421321)
print(iotDevice)

# Create a new Service Message instance to create the IoT Device on the server
serviceMessage = ServiceMessage("CREATE-DEVICE", iotDevice)

# Serialize the Service Message to a JSON string using the to_json method on the Service Message instance
msgFromClient = serviceMessage.to_json()
print(msgFromClient)

# Encode the JSON string to bytes using the str.encode method
bytesToSend = str.encode(msgFromClient)

# Create a TCP/IP socket associated with the address family IPv4 and the socket type SOCK_STREAM
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server using the specified address and port
    s.connect((HOST, PORT))

    # Send the bytes to the server to create the IoT Device
    s.sendall(bytesToSend)

    # Receive response data from the server using a buffer of 1024 bytes
    data = s.recv(1024)

    # Close the connection
    s.close()

    # Print the received data
    print('Received', repr(data))