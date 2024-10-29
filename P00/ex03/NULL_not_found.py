def NULL_not_found(object: any) -> int:
    ls = ["Nothing: None", "Cheese: nan", "Zero: 0 ", "Empty: ", "Fake: False"]
    type_list = [None, float("NaN"), 0, '', bool]
    for a in range(5):
        if a == 4 and type(object) is type_list[a]:
            print(ls[a], type(object))
            return 0
        elif type(object) is type(type_list[a]):
            if a == 3 and object:
                break
            else:
                print(ls[a], type(object))
                return 0
    print("Type not found")
    return 1
