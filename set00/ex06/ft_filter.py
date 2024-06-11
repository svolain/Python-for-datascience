class filter:
    def __init__(self, words, func, list):
        self.sequence = words
        self.func = func
        self.list = [x for x in words if func(x)]
"""
def ft_filter(function, sequence)->filter:
    list = filter([x for x in sequence if function(x)])
    return list

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