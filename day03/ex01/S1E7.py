from S1E9 import Character


class Baratheon(Character):
    """Barathon class,
    which inherit from Character class.
    Baratheon class has brown eyes and dark hair."""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Die method which set is_alive to false."""
        self.is_alive = False


class Lannister(Character):
    """Lannister class,
    which inherit from Character class.
    Lannister class has blue eyes and light hair."""

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Die method which set is_alive to false."""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive):
        new_instance = cls(first_name, is_alive)
        return new_instance
