from Projector import Projector

if __name__ == 'main':
    projectors = [Projector() for _ in range(3)]
    projectors[0] = Projector("Lenovo", "HDMI", "2420x2420", 12)
    projectors[1] = Projector("Acer", "VGA", "1000x1000", 7)
    projectors[2] = Projector.get_instance()

    for projector in projectors[:2]:
        print(f"Projector : {projector.str()}")

    Projector.print()