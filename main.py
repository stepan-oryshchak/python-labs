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

    # Отримання списку результатів виклику do_something() для кожного об'єкта
    result_list = projector_manager.get_results("do_something")
    print(result_list)

    # Отримання склейки об'єкта з його порядковим номером
    enumerated_list = projector_manager.get_enumerated()
    print(enumerated_list)

    # Отримання склейки об'єкта з результатом виклику do_something() за допомогою zip
    zipped_list = projector_manager.get_zipped_results("do_something")
    print(zipped_list)

    # Отримання словника з атрибутами, тип значень яких є int
    attribute_dict = projector_manager.get_attributes_by_type(int)
    print(attribute_dict)

    # Перевірка умови для всіх та будь-якого об'єкт
    condition_dict = projector_manager.check_conditions(lambda x: x.some_attribute > 10)
    print(condition_dict)
