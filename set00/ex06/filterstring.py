import sys
from ft_filter import filter

def main():
    try:
        assert sys.argv[1].isprintable() == True, 'AssertionError: the arguments are bad'
        assert sys.argv[2].isdigit() == True, 'AssertionError: the arguments are bad'
        assert len(sys.argv) == 3, 'AssertionError: the arguments are bad'
    except AssertionError as msg:
        print(msg)
        exit(1)
    words = sys.argv[1].split(' ')
    filtered = filter(words, (lambda x: len(x) >= int(sys.argv[2])), list)
    print(filtered)
    print(filtered.list)

if __name__=="__main__": 
    main()