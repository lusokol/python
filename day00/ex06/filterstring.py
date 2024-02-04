from ft_filter import ft_filter
import sys

def isEven(x):
    return True if x % 2 == 0 else False

def isUpperThanSix(x):
	return True if x > 6 else False

def main():
	if (len(sys.argv) != 3):
		raise AssertionError("Wrong number of arguments")
	elif (type(sys.argv[1]).__name__ != "str"):
		raise AssertionError("First argument must be a string")
	elif (type(sys.argv[2]).__name__ != "int"):
		try:
			n = int(sys.argv[2])
		except:
			raise AssertionError("Second argument must be an integer")

	#/////////////////////////:
	#NEXT
	words = [word for word in sys.argv[1].split() if len(word) >= n]
	print(words)
	#/////////////////////////:
	return 0
	# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	# print("List : " + str(lst) + "\n")
	# print("Function: None")
	# print(list(filter(None, lst)))
	# print(list(ft_filter(None, lst)))
	# print("\n")
	# print("Function: isEven")
	# print(list(filter(isEven, lst)))
	# print(list(ft_filter(isEven, lst)))
	# print("\n")
	# print("Function: isUpperThanSix")
	# print(list(filter(isUpperThanSix, lst)))
	# print(list(ft_filter(isUpperThanSix, lst)))


if __name__ == "__main__":
	try:
		main()
	except AssertionError as error:
		print("AssertionError: " + str(error))