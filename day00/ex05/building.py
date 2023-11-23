import sys
import string


def countCharTypes(text):
    """
    countCharTypes(str) --> void

    Count every digit, uppercase, lowercase, spaces, and punctuation
     elements in the text as input then display a summary about it
    """
    digit = sum(1 for char in text if char.isdigit())
    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())
    space = sum(1 for char in text if char.isspace())
    punctuation = sum(1 for char in text if char in string.punctuation)

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def askForText() -> str:
    """
    askForText(void) --> str

    Ask user to input something and return it.
    """
    text = input("What is the text to count?\n")
    return text


def main():
    """This main parse error and the text to analyze."""
    try:
        if (len(sys.argv) > 2):
            raise AssertionError("Too much arguments")
        elif (len(sys.argv) == 1):
            text = askForText()
        else:
            text = sys.argv[1]
        countCharTypes(text)
    except AssertionError as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()

# print (main.__doc__)
