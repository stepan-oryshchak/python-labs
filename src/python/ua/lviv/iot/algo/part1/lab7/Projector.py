class Projector:
    default_projector = None

    def __init__(self, model="", connected_device="", resolution="", lamp_hours=0):
        self.model = model
        self.connected_device = connected_device
        self.resolution = resolution
        self.lamp_hours = lamp_hours

    @staticmethod
    def get_instance():
        if Projector.default_projector is None:
            Projector.default_projector = Projector()
        return Projector.default_projector

    def add_input_device(self, device):
        self.connected_device = device
        return self.connected_device

    def disconnect_device(self):
        self.connected_device = "Empty"
        return self.connected_device

    def increase_lamp_hours(self, hours):
        self.lamp_hours += hours
        return self.lamp_hours

    def __str__(self):
        return f"Model: {self.model}, " \
               f"Connected Device: {self.connected_device}, " \
               f"Resolution: {self.resolution}, " \
               f"Lamp Hours: {self.lamp_hours}"


if __name__ == '__main__':
    first_projector = Projector()
    second_projector = Projector("Lenovo", "HDMI", "2420x2420", 12)
    third_projector = Projector("Acer", "VGA", "1000x1000", 7)
    fourth_projector = Projector.get_instance()

    projectors = [first_projector, second_projector, third_projector, fourth_projector]

    for projector in projectors:
        print(projector)

    second_projector.add_input_device("DVI")
    second_projector.increase_lamp_hours(3)
    print(second_projector)

    third_projector.disconnect_device()
    print(third_projector)
