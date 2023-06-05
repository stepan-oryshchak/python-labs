"""
Main script for managing projectors.
"""

from models.lamp_projector import LampProjector
from models.home_theater import HomeTheater
from models.projector import Projector
from manager.projector_manager import ProjectorManager
from manager.set_manager import SetManager


if __name__ == '__main__':
    projector_manager = ProjectorManager()
    projector_manager.add_projector(Projector("Apple", "DVI", "1920x1920", 15, "Xenon"))
    projector_manager.add_projector(LampProjector("Lenovo", "HDMI", "2420x2420", 12, "Sport", 350))
    projector_manager.add_projector(HomeTheater("Samsung", "HDMI", "8K", 10, "Entertainment", 200,
                                                "2023", 65, "2.0", 5))

    print("All objects")
    for projector in projector_manager.projectors:
        print(projector)
    print("\n")

    def lamp_hours_condition(some_projector):
        """
        Checks if a projector has a lamp_hours greater than 12.

        Args:
            some_projector (Projector): The projector object to check the lamp_hours for.

        Returns:
            bool: True if the projector's lamp_hours is greater than 12, False otherwise.
        """
        return some_projector.lamp_hours >= 16


    print("Test for condition capacity > 16")
    test_result = projector_manager.check_conditions(lamp_hours_condition)

    print("All projectors satisfy the lamp_hours condition: ", test_result["all"])
    print("Any projectors satisfy the lamp_hours condition: ", test_result["any"])
    print("\n")

    test_manager = ProjectorManager()
    test_manager.add_projector(Projector("Samsung", "HDMI", "2K", 19, "Some"))
    test_by_value = test_manager.get_attributes_by_type(int)
    print("List of attributes by value: ")
    for test_projector in test_by_value:
        print(test_projector)
    print("\n")

    get_enumerated = projector_manager.get_enumerated()
    print("Project number: ")
    for projector in get_enumerated:
        print(projector)
    print("\n")

    get_attributes_by_type = projector_manager.get_attributes_by_type(int)
    print("Project type int: ")
    for projector in get_attributes_by_type:
        print(projector)
    print("\n")

    zipped_list = projector_manager.get_zipped_results("do_something")
    print("Projector zipped: ")
    for projector in zipped_list:
        print(projector)
    print("\n")

    set_manager = SetManager(projector_manager)

    print("Number of items in Set Manager: ", len(set_manager))
    for item in set_manager:
        print(item)
