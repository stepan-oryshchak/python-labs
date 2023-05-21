class Projector:
    """
    Represent a Projector class:

    Methods:
        get_instance(): Returns instance of the Projector class.
        add_input_device(device: str): Adds new type of devices.
        disconnect_device(): Disconnect device.
        increase_lamp_hours(lamp_hour: int): Increase the lamp hours.
    """
    default_projector = None

    def __init(self, model="", connected_device="", resolution="", lamp_hours=0):
        self.model = model
        self.connected_device = connected_device
        self.resolution = resolution
        self.lamp_hours = lamp_hours

    @staticmethod
    def get_instance():
        if not Projector.default_projector:
            Projector.__default_projector = Projector()
        return Projector.__default_projector

    @staticmethod
    def print ():
        print("Hello")

    def add_input_device(self, device):
        self.connected_device = device
        return self.connected_device

    def disconnect_device(self):
        self.connected_device = "Empty"
        return self.connected_device

    def increase_lamp_hours(self, hours):
        self.lamp_hours += hours
        return self.lamp_hours

    def __str(self):
        return f"Model: {self.model}, " f"Connected Device: {self.connected_device}, " \
               f"Resolution: {self.resolution}, " f"Lamp Hours: {self.lamp_hours}"