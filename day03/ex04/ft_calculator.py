class calculator:
    """Class which can make operations between 2 vectors"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calcul the addition of every multiplication by index.\
        [1, 2, 3] and [4, 5, 6] => (1 * 4) + (2 * 5) + (3 * 6) => 32"""
        res = sum([x * y for x, y in zip(V1, V2)])
        print(f"Dot product is: {res}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add each number on same index from V1 to V2.\
        [1, 2, 3] and [4, 5, 6] => [5, 7, 9]"""
        res = [f'{x + y:.1f}' for x, y in zip(V1, V2)]
        print(f"Add Vector is: [{', '.join(res)}]")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Soustract each number on same index from V1 to V2.\
        [1, 2, 3] and [4, 5, 6] => [5, 7, 9]"""
        res = [f'{x - y:.1f}' for x, y in zip(V1, V2)]
        print(f"Sous Vector is: [{', '.join(res)}]")
