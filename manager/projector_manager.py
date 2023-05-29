class ProjectorManager:
    """
    ProjectorManager class manages projectors.

    Methods:
        add_projectors(): Creates a list of projectors.
    """

    def __init__(self):
        self.projectors = []

    def add_projector(self, projector):
        """
        Adds a projector to the manager's collection.

        Args:
            projector: The projector to add.

        """
        self.projectors.append(projector)
