def square(x: int | float) -> int | float:
    return x * x


def pow(x: int | float) -> int | float:
    return x ** x


def outer(x: int | float, function) -> object:
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
