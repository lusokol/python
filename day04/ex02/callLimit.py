def callLimit(limit: int):
    """
    Decorator which limit the number of function's call
    """
    count = 0

    def callLimiter(function):

        def limit_function(*args: any, **kwds: any):
            nonlocal count
            if (count < limit):
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
