def ft_filter(function, sequence)->list:
    list = [x for x in sequence if function(x)]
    return list
"""
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False

sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

filtered = ft_filter(fun, sequence)
 
print('The filtered letters are:')
for s in filtered:
    print(s)
"""