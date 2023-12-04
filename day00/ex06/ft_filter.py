def ft_filter(function, iterable):
    """
ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    if function != None:
        return iter([obj for obj in iterable if function(obj)])#True if function(i in iterable) else False
    else:
        return iter([obj for obj in iterable if obj != False])#return True if i in iterable else False