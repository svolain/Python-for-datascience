def all_thing_is_obj(object: any) -> int:
    if type(object) is list:
        print('List : ', end='')
    elif type(object) is dict:
        print('Dict : ', end='')
    elif type(object) is set:
        print('Set : ', end='')
    elif type(object) is tuple:
        print('Tuple : ', end='')
    elif type(object) is str:
        print(object, "is in the kitchen : ", end='')
    else:
        print("type not found",)
        return (42)
    print(object.__class__)
    return (42)

"""
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))
"""