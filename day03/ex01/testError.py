from S1E9 import Character


try:
    hodor = Character("hodor")
except TypeError as error:
    print(f"TypeError: {error}")
