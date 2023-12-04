from ft_filter import ft_filter

def isEven(x):
    return True if x % 2 == 0 else False

def main():
    print(list(filter(None, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
    print("\n")
    print(list(ft_filter(None, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
    print("\n")
    print(list(filter(isEven, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
    print("\n")
    print(list(ft_filter(isEven, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
    print("\n")
    print(filter(isEven, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print("\n")
    print(ft_filter(isEven, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


if __name__ == "__main__":
    main()