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

    for projector in projector_manager.projectors:
        print(projector)
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
