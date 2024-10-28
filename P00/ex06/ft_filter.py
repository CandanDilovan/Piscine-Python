
def ft_filter(fun, list):
    """filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of\
    iterable for which function(item)
    is true. If function is None, return the items that are true."""
    if callable(fun):
        filtered = [x for x in list if fun(x)]
    else:
        filtered = [x for x in list if x]
    return (filtered)
