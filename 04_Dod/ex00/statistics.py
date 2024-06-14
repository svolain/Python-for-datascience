import sys

def ft_statistics(*args: any, **kwargs: any) -> None:
    lenArgs = len(args)
    lenKwargs = len(kwargs)
    if lenArgs < 1:
        return 
    if lenKwargs < 1:
        return
    
    list_args = list(args)
    list_args.sort()
    s = 0
    for arg in args:
        s += arg
    mean = s / lenArgs
    for key, values in kwargs.items():
        match values:
            case 'mean':
                print('mean :', mean)
            case 'median':
                list_args = list(args)
                list_args.sort()
                mid = lenArgs / 2
                print('median :', list_args[int(mid)])
            case 'quartile':
                q1 = lenArgs / 3
                q3 = lenArgs / 1.5
                print('q1 & q3:', q1, q3)
                print('quartile : [', list_args[int(q1)], ',', list_args[int(q3)], ']')
            case 'std':
                var = sum((x - mean) ** 2 for x in list_args) / lenArgs
                psd = var ** 0.5
                print("std :", psd)
            case 'var':
                var = sum((x - mean) ** 2 for x in list_args) / lenArgs
                print('var :', var)
