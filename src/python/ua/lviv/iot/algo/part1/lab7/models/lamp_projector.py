from abstract_projector import AbstractProjector


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

    def __init__(self, model="", connected_device="", resolution="", lamp_hours=0, display_mode="", max_lamp_hours=0):
        super().__init__(model, connected_device, resolution, lamp_hours)
        self.display_mode = display_mode
        self.max_lamp_hours = max_lamp_hours

    def set_display_mode(self, mode):
        self.display_mode = mode

    def get_remaining_working_hours(self):
        return self.max_lamp_hours - self.lamp_hours
