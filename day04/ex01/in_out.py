def square(x: int | float) -> int | float:
    """
    Calcul the square of x and return it
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    Calcul the power of x^x and return it
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Execute the provided function, update the value, and return the result.
    The value pass into the given function each time outer is call.
    """
    count = x

    def inner() -> float:
        nonlocal count
        try:
            res = function(count)
            count = res
            return res
        except TypeError as err:
            print(f"TypeError: {err}")
            exit()
    return inner
