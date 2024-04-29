from abc import ABC, abstractmethod


class Character(ABC):
    """Character class which take 2 arguments, first_name and is_alive"""
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """Stark Class which inherit from Character abstract class. \
It has 2 variables, first_name and is_alive."""
    def __init__(self, first_name, is_alive=True):
        """Constructor of Stark class"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Die method which set is_alive to false."""
        self.is_alive = False
