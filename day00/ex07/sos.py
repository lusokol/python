import sys


def main():
    """
    This program converts any single alphanumeric character into morse.
    """
    morse = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
             "E": ".", "F": "..-.", "G": "--.", "H": "....",
             "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
             "M": "--", "N": "-.", "O": "---", "P": ".--.",
             "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
             "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
             "Y": "-.--", "Z": "--..", "0": "-----",
             "1": ".----", "2": "..---", "3": "...--",
             "4": "....-", "5": ".....", "6": "-....",
             "7": "--...", "8": "---..", "9": "----.", " ": "/"}
    try:
        for letter in sys.argv[1].upper():
            assert letter in morse, (
                f"Character '{letter}' not found in Morse dictionary."
            )
        translated = (" ".join(morse[letter] for letter
                               in sys.argv[1].upper()))
        print(translated)
    except AssertionError as error:
        print(f"AssertionError: {error.args[0]}")


if __name__ == "__main__":
    main()
