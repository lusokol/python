from abc import ABC, abstractmethod


class Character(ABC):
    """Character class which take 2 arguments, first_name and is_alive"""
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        pass

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.hairs}', '{self.eyes}')"


class Stark(Character):
    """Stark Class which inherit from Character abstract class. \
It has 2 variables, first_name and is_alive."""
    def __init__(self, firstName, isAlive=True):
        """Constructor of Stark class"""
        self.first_name = firstName
        self.is_alive = isAlive

    def die(self):
        """Die method which set is_alive to false."""
        self.is_alive = False
