import sys

def is_Even_or_Odd(argument):
    if (len(argument) == 1) : return 1
    elif (len(argument) >= 3) :
        print(f"AssertionError: more than one argument is provided")
        return 1
    try:
        number = int(argument[1])
        if (number % 2 == 0) : print("I'm Even.")
        else : print("I'm Odd.")
    except:
        print(f"AssertionError: argument is not an integer")

is_Even_or_Odd(sys.argv)

#print(type(int(sys.argv[1])))