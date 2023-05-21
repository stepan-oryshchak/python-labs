class ProjectorManager:
    """
    ProjectorManager class manages projectors.

    Methods:
        create_projectors(): Creates a list of projectors.
        print_projectors(projectors: List[AbstractProjector]): Prints the projectors in the list.
    """

    def __init__(self):
        self.projectors = []

    def add_projector(self, projector):
        """
        Adds a projector to the manager's collection.

        Args:
            Projectors (AbstractProjector): The projector to add.

        """
        self.projectors.append(projector)
