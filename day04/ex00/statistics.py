import math

def mean(*args: any):
    print(f"mean : {sum(args[0]) / len(args[0])}")

def median(*args: any):
    lst = list(args[0])
    lst.sort()
    print(f"median : {lst[math.floor(len(lst) / 2)]}")

def quartile(*args: any):
    lst = list(args[0])
    lst.sort()
    q1 = lst[math.floor(len(lst) / 4)]
    q3 = lst[math.floor(len(lst) / 4) * 3]
    qrtl = [q1, q3]
    formatted_qrtl = [f"{x:.1f}" for x in qrtl]
    print(f"quartile : [{formatted_qrtl[0]}, {formatted_qrtl[1]}]")

def ft_statistics(*args: any, **kwargs: any) -> None:
    mean(args)
    median(args)
    quartile(args)