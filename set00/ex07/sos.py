import sys
def getMorse(str)->list:
    NESTED_MORSE = {    ' ': '/ ',
                        'A': '.-',
                        'B': '-...',
                        'C': '-.-.', 
                        'D': '-..',
                        'E': '.',
                        'F': '..-.',
                        'G': '--.',
                        'H': '....',
                        'I': '..',
                        'J': '.---',
                        'K': '-.-',
                        'L': '.-..',
                        'M': '--',
                        'N': '-.',
                        'O': '---',
                        'P': '.--.',
                        'Q': '--.-',
                        'R': '.-.',
                        'S': '...',
                        'T': '-',
                        'U': '..-',
                        'V': '...-',
                        'W': '.--',
                        'X': '-..-',
                        'Y': '-.--',
                        'Z': '--..',
                        '0': '-----', 
                        '1': '.----',
                        '2': '..---',
                        '3': '...--',
                        '4': '....-',
                        '5': '.....',
                        '6': '-....',
                        '7': '--...',
                        '8': '---..',
                        '9': '----.'
                    }
    list = []
    for i in str.upper():
        if i in NESTED_MORSE:
            list.append(NESTED_MORSE[i])
        else:
            raise AssertionError('AssertionError: the arguments are bad')
    return ' '.join(list)

def main():
    try:
        
        if len(sys.argv) != 2:
            raise AssertionError('AssertionError: the arguments are bad')
        morse = getMorse(sys.argv[1])
        print(morse)
    except AssertionError as msg:
        print(msg)

if __name__=="__main__": 
    main()