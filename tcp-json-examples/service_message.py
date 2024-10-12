import json

class ServiceMessage:
    """ Service Message Class describing the action command and the target IoT Device
    For example this class can be used to describe a CREATED DEVICE request on the server """

    def __init__(self, action_command, iot_device):
        """ Initialize the Service Message with the provided action command and IoT Device """
        self.action_command = action_command
        self.iot_device = iot_device

    def __str__(self):
        """ Return a string representation of the Service Message """
        return f"Action Command: {self.action_command} - Target IoT Device: {self.iot_device}"

    def to_json(self):
        """ Serialize the Service Message to a JSON string """
        return json.dumps(self, default=lambda o: o.__dict__)
