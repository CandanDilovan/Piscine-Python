def all_thing_is_obj(object: any) -> int:
    str_list = ["List", "Tuple", "Set", "Dict", "str"]
    type_list = [list, tuple, set, dict, str]
    for a in range(5):
        if type(object) == type_list[a]:
            if a == 4:
                print(object, "is in the kitchen :", type(object))
                return 42
            else:
                print(str_list[a], ":", type(object))
                return 42
    print("Type not found")
    return 42