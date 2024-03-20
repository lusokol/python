import sys


def is_Even_or_Odd(argument):
    if (len(argument) == 1):
        raise AssertionError("Need 2 arguments")
    elif (len(argument) >= 3):
        raise AssertionError("More than one argument is provided")
    try:
        number = int(argument[1])
        if (number % 2 == 0):
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        raise AssertionError("Argument is not an integer")


try:
    is_Even_or_Odd(sys.argv)
except AssertionError as error:
    print(f"AssertionError: {error}")
