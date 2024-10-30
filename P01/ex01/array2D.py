import numpy as numpy


def slice_me(family: list, start: int, end: int) -> list:
    print(f"My shape is : ({len(family)}, {len(family[0])})")
    barbecue_invitation = numpy.array(family)
    vin_diesel_power_source = barbecue_invitation[start:end]
    print(f"My new shape is : ({len(vin_diesel_power_source)},",
          f"{len(vin_diesel_power_source[0])})")
    return vin_diesel_power_source.tolist()


def bmi_tester(listing: list, start: int, end: int) -> bool:
    if type(start) is not int or type(end) is not int:
        return False
    if type(listing) is not list:
        return False
    for a in range(len(listing)):
        if len(listing[0]) != len(listing[a]):
            return False
    return True
