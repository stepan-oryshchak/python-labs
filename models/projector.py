"""
This module defines the Projector class, which represents a projector device.

Classes:
    Projector: Represents a projector device.

"""

from models.abstract_projector import AbstractProjector


# pylint: disable=too-many-arguments
class Projector(AbstractProjector):
    """
    Represents a Projector class.

    Attributes:
        default_projector: Stores the default Projector instance.

    Methods:
        get_instance(): Returns an instance of the Projector class.
        add_input_device(device: str): Adds a new type of device.
        disconnect_device(): Disconnects the device.
        increase_lamp_hours(lamp_hour: int): Increases the lamp hours.

    Overrides:
        __str__(): Returns a string representation of the Projector object.
        do_something(): Performs an action and returns a message.
    """

    default_projector = None

    def __init__(self, model="", connected_device="", resolution="", lamp_hours=0, lens=""):
        """
        Initialize a Projector object.

        Args:
            model (str): The model of the projector.
            connected_device (str): The connected device.
            resolution (str): The resolution of the projector.
            lamp_hours (int): The current lamp hours of the projector.
            lens (str): The lens information of the projector.
        """
        super().__init__(model, connected_device, resolution, lamp_hours)
        self.model = model
        self.connected_device = connected_device
        self.resolution = resolution
        self.lamp_hours = lamp_hours
        self.lens = lens
        self.some_attribute = 0

    @staticmethod
    def get_instance():
        """
        Get an instance of the Projector class.

        Returns:
            Projector: The Projector instance.
        """
        if not Projector.default_projector:
            Projector.default_projector = Projector()
        return Projector.default_projector

    @staticmethod
    def print():
        """
        Print a message.

        This is a static method that prints a message.
        """
        print("Hello")

    def add_input_device(self, device):
        """
        Add a new input device.

        Args:
            device (str): The new device to be added.

        Returns:
            str: The connected device.
        """
        self.connected_device = device
        return self.connected_device

    def disconnect_device(self):
        """
        Disconnect the device.

        Returns:
            str: The connected device set to "Empty".
        """
        self.connected_device = "Empty"
        return self.connected_device

    def increase_lamp_hours(self, hours):
        """
        Increase the lamp hours.

        Args:
            hours (int): The number of hours to increase.

        Returns:
            int: The updated lamp hours.
        """
        self.lamp_hours += hours
        return self.lamp_hours

    def get_remaining_working_hours(self):
        """
        Get the remaining working hours.

        This method is not implemented yet.
        """

    def __str__(self):
        """
        Return a string representation of the Projector object.

        Returns:
            str: The string representation of the Projector object.
        """
        return f"{super().__str__()}, " \
               f"Resolution: {self.lens}"

    def do_something(self):
        """
        Perform an action and return a message.

        Returns:
            str: A message indicating that something is being done.
        """
        return "Run projector"
