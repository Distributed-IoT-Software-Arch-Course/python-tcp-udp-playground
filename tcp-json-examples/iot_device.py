import json

class IoTDevice:
    """ IoT Device Class describing the device properties """

    def __init__(self, device_id, manufacturer, software_version, latitude, longitude):
        """ Initialize the IoT Device with the provided properties """

        self.device_id = device_id
        self.manufacturer = manufacturer
        self.software_version = software_version
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        """ Return a string representation of the IoT Device """
        return f"DeviceId: {self.device_id} - Manufacturer: {self.manufacturer} - Software Version: {self.software_version} - Lat/Lng: {self.latitude}/{self.longitude}"

    def to_json(self):
        """ Serialize the IoT Device to a JSON string """
        return json.dumps(self, default=lambda o: o.__dict__)
