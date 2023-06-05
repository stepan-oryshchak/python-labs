"""
Abstract projector class
"""

from abc import ABC, abstractmethod


class AbstractProjector(ABC):
    """
    AbstractProjector class represents an abstract projector.

    Methods:
        get_instance(): Returns an instance of the AbstractProjector class.
        add_input_device(device: str): Adds a new type of device.
        disconnect_device(): Disconnects the device.
        increase_lamp_hours(lamp_hours: int): Increases the lamp hours.
        get_remaining_working_hours(): Returns the remaining working hours of the projector.
    """
    default_projector = None
    WORKING_HOURS_PER_YEAR = 3650

    def __init__(self, model="", connected_device="", resolution="", lamp_hours=0):
        self.model = model
        self.connected_device = connected_device
        self.resolution = resolution
        self.lamp_hours = lamp_hours
        self.some_attribute = 0

    @abstractmethod
    def get_remaining_working_hours(self):
        """

        :return:
        """
        pass

    def __str__(self):
        return f"Model: {self.model}, " \
               f"Connected Device: {self.connected_device}, " \
               f"Resolution: {self.resolution}, " \
               f"Lamp Hours: {self.lamp_hours}"

    @abstractmethod
    def do_something(self):
        """

        :return:
        """
        return "Doing something"
