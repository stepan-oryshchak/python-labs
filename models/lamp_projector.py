"""
Lamp projector class
"""

from models.abstract_projector import AbstractProjector


# pylint: disable=too-many-arguments
class LampProjector(AbstractProjector):
    """
    LampProjector class represents a lamp projector.

    Additional Attributes:
        lamp_hours: The number of hours the lamp has been used.
        display_mode: The display mode of the projector (sport, active, presentation).
        max_lamp_hours: The maximum allowed lamp hours.

    Methods:
        set_display_mode(mode: str): Sets the display mode of the projector.
        get_remaining_working_hours(): Returns the remaining working hours of the lamp projector.
    """

    def __init__(self, model="", connected_device="", resolution="", lamp_hours=0,
                 display_mode="", max_lamp_hours=0):
        super().__init__(model, connected_device, resolution, lamp_hours)
        self.display_mode = display_mode
        self.max_lamp_hours = max_lamp_hours
        self.some_attribute = 0

    def set_display_mode(self, mode):
        """

        :param mode:
        :return:
        """
        self.display_mode = mode

    def get_remaining_working_hours(self):
        """

        :return:
        """
        return self.max_lamp_hours - self.lamp_hours

    def __str__(self):
        return f"{super().__str__()}, " \
               f"Resolution: {self.display_mode}, " f"Lens: {self.max_lamp_hours}"

    def do_something(self):
        """

        :return:
        """
        return "Run lamp projector"
