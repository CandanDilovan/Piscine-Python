def give_bmi(height: list[int | float], weight: list[int | float]):
    assert bmi_tester(height, weight), "Wrong arguments"
    bmi_lst = [weight[0] / (height[0] * height[0]),
               weight[1] / (height[1] * height[1])]
    return bmi_lst


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    assert bmi_tester(bmi, limit), "Wrong arguments"
    fatty = [False, False]
    for a in range(2):
        if bmi[a] < limit:
            fatty[a] = True
    return (fatty)


def bmi_tester(list1: list[int | float], list2: list[int | float]) -> bool:
    if len(list1) > 2:
        return False
    if type(list2) is list and len(list2) > 2:
        return False
    for a in range(2):
        if not isinstance(list1[a], (int, float)):
            return False
        if type(list2) is list and not isinstance(list2[a], (int, float)):
            return False
    return True
