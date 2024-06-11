"""
give_bmi takes 2 lists of integers or floats in input and returns a list of BMI values
"""

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:       
        if len(height) != len(weight):
            raise AssertionError('Error: the lists are not the same size')
        list = []
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
                raise AssertionError('Error: the lists must have type int or float')
            list.append(w / (h * h))
        return list
    except AssertionError as msg:
        print(msg)
        exit()
    return []

"""
apply_limit accepts a list of integers or floats and an integer representing
a limit as parameters. It returns a list of booleans (True if above the limit)
"""

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        list = []
        for i in bmi:
            if not isinstance(i, (int, float)):
                raise AssertionError('Error: the lists must have type int or float')
            if i > limit:
                list.append(True)
            else:
                list.append(False)
        return list
    except AssertionError as msg:
        print(msg)
        exit()
    return []
