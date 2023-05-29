class ProjectorManager:
    """
    ProjectorManager class manages projectors.

    Methods:
        add_projector(): Adds a projector to the manager's collection.
        __len__(): Returns the number of projectors in the manager.
        __getitem__(): Returns the projector at the specified index.
        __iter__(): Returns an iterator over the projectors.
        get_results(): Returns a list of results from calling a specific method on each projector.
        get_enumerated(): Returns a concatenation of each projector with its index.
        get_zipped_results(): Returns a zip of each projector with the results of a specific method.
        get_attributes_by_type(): Returns a dictionary of attributes filtered by a specific data type.
        check_conditions(): Returns a dictionary indicating if all or any projectors satisfy a given condition.
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

    def __len__(self):
        """
        Returns the number of projectors in the manager.
        """
        return len(self.projectors)

    def __getitem__(self, index):
        """
        Returns the projector at the specified index.

        Args:
            index: The index of the projector to retrieve.
        """
        return self.projectors[index]

    def __iter__(self):
        """
        Returns an iterator over the projectors.
        """
        return iter(self.projectors)

    def get_results(self, method_name):
        """
        Returns a list of results from calling a specific method on each projector.

        Args:
            method_name: The name of the method to call on each projector.
        """
        return [getattr(projector, method_name)() for projector in self.projectors]

    def get_enumerated(self):
        """
        Returns a concatenation of each projector with its index.
        """
        return [f"{index}: {projector}" for index, projector in enumerate(self.projectors)]

    def get_zipped_results(self, method_name):
        """
        Returns a zip of each projector with the results of a specific method.

        Args:
            method_name: The name of the method to call on each projector.
        """
        return list(zip(self.projectors, self.get_results(method_name)))

    def get_attributes_by_type(self, data_type):
        """
        Returns a dictionary of attributes filtered by a specific data type.

        Args:
            data_type: The data type to filter attributes by.
        """
        return {key: value for projector in self.projectors for key, value in projector.__dict__.items() if isinstance(value, data_type)}

    def check_conditions(self, condition):
        """
        Returns a dictionary indicating if all or any projectors satisfy a given condition.

        Args:
            condition: The condition to check for each projector.
        """
        return {"all": all(condition(projector) for projector in self.projectors), "any": any(condition(projector) for projector in self.projectors)}
