from ft_filter import ft_filter
import sys


def isEven(x):
    """
isEven(int) => boolean

return True if parameter is even, else return False
    """
    return True if x % 2 == 0 else False


def isUpperThan(x, y):
    """
isUpperThan(int, int) => boolean

return True if first parameter is upper than second, else return False
    """
    return True if x > y else False


def main():
    """This main parse error and arguments"""
    if (len(sys.argv) != 3):
        raise AssertionError("Wrong number of arguments")
    elif (type(sys.argv[1]).__name__ != "str"):
        raise AssertionError("First argument must be a string")
    elif (type(sys.argv[2]).__name__ != "int"):
        try:
            n = int(sys.argv[2])
        except ValueError:
            raise AssertionError("Second argument must be an integer")

    # /////////////////////////:
    words = ft_filter(lambda word: len(word) > n, sys.argv[1].split())
    print(list(words))
    # /////////////////////////:
    return 0


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print("AssertionError: " + str(error))
