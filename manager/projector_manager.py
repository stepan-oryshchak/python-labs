"""
Representing a projector manager.
"""


# pylint: disable = too-many-arguments
# pylint: disable = line-too-long
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
        check_conditions(): Returns a dictionary indicating if all or any projectors satisfy
         a given condition.
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
        Returns a concatenation of each projector's object and its index in the manager's collection.

        Returns:
            list: A list of tuples containing each projector's object and its index.
        """
        return [(index + 1, projector) for index, projector in enumerate(self.projectors)]

    def get_zipped_results(self, method_name):
        """
        Returns a zip of each projector with the results of a specific method.

        Args:
            method_name: The name of the method to call on each projector.
        """
        return list(zip(self.projectors, self.get_results(method_name)))

    def check_conditions(self, condition_func):
        """
        Returns a dictionary indicating if all and any projectors satisfy a certain condition.

        Returns:
            dict: A dictionary with keys all and any indicating if all and any projectors satisfy a certain condition
        """
        all_satisfy = all(condition_func(projector) for projector in self.projectors)
        any_satisfy = any(condition_func(projector) for projector in self.projectors)
        return {"all": all_satisfy, "any": any_satisfy}

    def get_attributes_by_type(self, data_type):
        """
        Returns a dictionary with attributes and values of each projector that have values of the specified type.

        Args:
            data_type (type): The type of values to filter attributes by.

        Returns:
            dict: A dictionary with attributes and values of each projector that have values of the specified type.
        """
        return {attribute: type_of_attr for obj in self.projectors for attribute, type_of_attr in obj.__dict__.items()
                if isinstance(type_of_attr, data_type)}
