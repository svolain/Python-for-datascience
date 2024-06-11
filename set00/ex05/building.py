import sys

def count_characters(str):
    chars = 0
    upperCase = 0
    lowerCase = 0
    punctuation = 0
    space = 0
    digits = 0

    for i in str:
        if i.isdigit():
            digits += 1
        elif i.isupper():
            upperCase += 1
        elif i.islower():
            lowerCase += 1
        elif i.isspace():
            space += 1
        elif i in '!"#$%&\'()*+, -./:;<=>?@[\]^_`{|}~':
            punctuation += 1
        chars += 1
    print('The text contains ', chars, ' characters:')
    print(upperCase, ' upper letters')
    print(lowerCase, ' lower letters')
    print(punctuation, ' punctuation marks')
    print(space, ' spaces')
    print(digits, ' digits')

        

def main():
    if len(sys.argv) > 2:
        print('AssertionError')
        exit()
    elif len(sys.argv) < 2:
        arg = input("What is the text to count?\n")
        arg += "\n"
        count_characters(arg)
    else:
        arg = sys.argv[1]
        count_characters(arg)

if __name__=="__main__": 
    main()