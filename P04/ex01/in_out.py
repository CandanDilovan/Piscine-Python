def square(x: int | float) -> int | float:
    return x * x


def pow(x: int | float) -> int | float:
    return x ** x


def outer(x: int | float, function) -> object:
    count = 0
    count = x

    def inner() -> float:
        nonlocal count
        count = function(count)
        return count

    return inner
