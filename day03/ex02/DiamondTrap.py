from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Diamond class from Baratheon and Lannister"""
    def __init__(self, first_name, is_alive=True):
        """Initialize King's class"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """Take one argument to change eyes's color"""
        self.eyes = color

    def set_hairs(self, color):
        """Take one argument to change hairs's color"""
        self.hairs = color

    def get_eyes(self):
        """Return eyes color"""
        return self.eyes

    def get_hairs(self):
        """Return hairs color"""
        return self.hairs
