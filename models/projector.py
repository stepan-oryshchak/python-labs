from .abstract_projector import AbstractProjector


class Projector(AbstractProjector):
    """
    Represent a Projector class:

    Methods:
        get_instance(): Returns instance of the Projector class.
        add_input_device(device: str): Adds new type of devices.
        disconnect_device(): Disconnect device.
        increase_lamp_hours(lamp_hour: int): Increase the lamp hours.
    """

    default_projector = None

    def __init__(self, model="", connected_device="", resolution="", lamp_hours=0, lens=""):
        super().__init__(model, connected_device, resolution, lamp_hours)
        self.model = model
        self.connected_device = connected_device
        self.resolution = resolution
        self.lamp_hours = lamp_hours
        self.lens = lens

    @staticmethod
    def get_instance():
        if not Projector.default_projector:
            Projector.default_projector = Projector()
        return Projector.default_projector

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

    def get_remaining_working_hours(self):
        pass

    def __str__(self):
        return f"{super().__str__()}, " \
               f"Resolution: {self.lens}"
