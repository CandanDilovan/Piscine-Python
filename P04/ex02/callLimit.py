def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            nonlocal count
            count += 1
            if limit == count:
                print("Error:", function, "call too many times")
            else:
                function()
        return limit_function
    return callLimiter
