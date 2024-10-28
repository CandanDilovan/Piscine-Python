def NULL_not_found(object: any) -> int:
    str_list = ["Nothing: None", "Cheese: nan", "Zero: 0 ", "Empty: ", "Fake: False"]
    type_list = [None, float("NaN"), 0, '', bool]
    for a in range(5):
        if a == 4 and type(object) == type_list[a]:
                print(str_list[a], type(object))
                return 0
        elif type(object) == type(type_list[a]):
            if a == 3 and object:
                break
            else:
                print(str_list[a], type(object))
                return 0
    print("Type not found")
    return 1