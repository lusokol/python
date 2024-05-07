import math


def mean(data):
    """
    Return mean of the data
    """
    return sum(data) / len(data)


def median(args):
    """
    Return median of the data
    """
    args.sort()
    return args[math.floor(len(args) / 2)]


def quartile(args):
    """
    Return quartile of the data
    """
    args.sort()
    q1 = args[math.floor(len(args) / 4)]
    q3 = args[math.floor(len(args) / 4) * 3]
    return [q1, q3]


def variance(args):
    """
    Return variance of the data
    """
    m = mean(args)
    return sum((x - m) ** 2 for x in args) / len(args)


def std(args):
    """
    Return standar deviation of the data
    """
    return variance(args) ** 0.5


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Calcul and print some stats about args
    """
    args = list(args)
    for key, value in kwargs.items():
        try:
            match (value):
                case "mean":
                    print(f"mean : {mean(args)}")
                case "median":
                    print(f"median : {median(args)}")
                case "quartile":
                    print(f"quartile : [\
{', '.join([f'{arg:.1f}' for arg in quartile(args)])}]")
                case "std":
                    print(f"std : {std(args)}")
                case "var":
                    print(f"var : {variance(args)}")
                case _:
                    break
        except ZeroDivisionError:
            print("ERROR")
        except IndexError:
            print("ERROR")
