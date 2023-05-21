from lamp_projector import LampProjector


class HomeTheater(LampProjector):
    """
    HomeTheater class represents a home theater system.

    Additional Attributes:
        year_of_sale: The year of sale of the home theater.
        screen_size: The screen size in inches.
        smart_tv_version: The supported smart TV version.
        warranty_years: The number of years the warranty is valid.

    Methods:
        get_remaining_working_hours(): Returns the remaining working hours of the home theater.
    """

    def __init__(self, model="", connected_device="", resolution="", lamp_hours=0, display_mode="", max_lamp_hours=0,
                 year_of_sale="", screen_size=0, smart_tv_version="", warranty_years=0):
        super().__init__(model, connected_device, resolution, lamp_hours, display_mode, max_lamp_hours)
        self.year_of_sale = year_of_sale
        self.screen_size = screen_size
        self.smart_tv_version = smart_tv_version
        self.warranty_years = warranty_years

    def get_remaining_working_hours(self):
        return self.warranty_years * self.WORKING_HOURS_PER_YEAR
