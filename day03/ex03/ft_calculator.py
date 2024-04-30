class calculator:
    """Class which contain a vector. You can do some simple operations with it\
 : +, -, *, /"""
    def __init__(self, vector):
        """Calculator's constructor"""
        self.vector = vector

    def print(self):
        """Print Vector in the terminal."""
        print(self.vector)

    def __add__(self, object) -> None:
        """Addition whole vector by item"""
        self.vector = [item + object for item in self.vector]
        self.print()

    def __mul__(self, object) -> None:
        """Multiply whole vector by item"""
        self.vector = [item * object for item in self.vector]
        self.print()

    def __sub__(self, object) -> None:
        """Substract whole vector by item"""
        self.vector = [item - object for item in self.vector]
        self.print()

    def __truediv__(self, object) -> None:
        """Divide whole vector by item"""
        try:
            self.vector = [item / object for item in self.vector]
            self.print()
        except ZeroDivisionError as error:
            print(f"ZeroDivisionError: {error}")
