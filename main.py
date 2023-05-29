"""
Main script for managing projectors.
"""

from models.lamp_projector import LampProjector
from models.home_theater import HomeTheater
from models.projector import Projector
from manager.projector_manager import ProjectorManager


if __name__ == '__main__':
    projector_manager = ProjectorManager()
    projector_manager.add_projector(Projector("Apple", "DVI", "1920x1920", 15, "laser"))
    projector_manager.add_projector(LampProjector("Lenovo", "HDMI", "2420x2420", 12, "sport", 350))
    projector_manager.add_projector(HomeTheater("Samsung", "HDMI", "8K", 10, "entertainment", 200,
                                                "2023", 65, "2.0", 5))
    projector_manager.add_projector(HomeTheater("Sony", "HDMI", "4K", 20, "presentation", 300,
                                                "2022", 65, "2.0", 3))

    for projector in projector_manager.projectors:
        print(projector)
    print("\n")
