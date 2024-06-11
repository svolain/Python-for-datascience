def NULL_not_found(object: any) -> int:
    if object is None:
        print('Nothing: None ', end='')
    elif object != object:
        print('Cheese: nan ', end='')
    elif object == 0 and object.__class__ is int:
        print('Zero: 0 ', end='')
    elif object == False and object.__class__ is bool:
        print('Fake: False ', end='')
    elif object == '':
        print('Empty: ', end='')
    else:
        print('Type not found')
        return (1)
    print(object.__class__)
    return (0)

"""
Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
"""