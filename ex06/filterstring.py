import sys
from ft_filter import ft_filter

def main():
    if sys.argv[1].isprintable() == False:
        print('AssertionError: the arguments are bad')
    if sys.argv[2].isdigit() == False:
        print('AssertionError: the arguments are bad')
    if len(sys.argv) != 3:
        print('AssertionError: the arguments are bad')
    words = sys.argv[1].split(' ')
    sequence = ft_filter(lambda x: len(x) >= int(sys.argv[2]), words)
    print(list(sequence))

if __name__=="__main__": 
    main()