def ft_statistics(*args: any, **kwargs: any) -> None:
    lst_method = ["mean", "median", "quartile", "std", "var"]
    lst_function = [ft_mean, ft_median, ft_quartile, ft_std, ft_var]
    for key, value in kwargs.items():
        if len(args) == 0:
            print("ERROR")
        else:
            for a in range(len(lst_method)):
                if value == lst_method[a]:
                    result = lst_function[a](args)
                    print(lst_method[a], ":", result)


def ft_mean(lst):
    a = 0
    for b in range(len(lst)):
        a += lst[b]
    return a / len(lst)


def ft_median(lst):
    lst = sorted(lst)
    middle = round(len(lst) / 2)
    if len(lst) % 2 == 0:
        median = (lst[middle - 1] + lst[middle]) / 2
        return median
    else:
        return lst[middle]


def ft_quartile(lst):
    q1 = round(0.25 * len(lst))
    q3 = int(0.75 * len(lst))
    lst = sorted(lst)
    quartille = [float(lst[q1]), float(lst[q3])]
    return quartille


def ft_std(lst):
    total = 0
    mean = ft_mean(lst)
    for a in range(len(lst)):
        deviation = lst[a] - mean
        square = deviation * deviation
        total += square
    std = total / (len(lst))
    std = std ** 0.5
    return std


def ft_var(lst: int):
    total = 0
    mean = ft_mean(lst)
    for a in range(len(lst)):
        deviation = lst[a] - mean
        square = deviation * deviation
        total += square
    var = total / (len(lst))
    return var
