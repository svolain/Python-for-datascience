import sys

if len(sys.argv) < 2:
    exit()
elif len(sys.argv) > 2:
    print('AssertionError: more than one argument is provided')
    exit()
elif not sys.argv[1].lstrip("-").isnumeric():
    print('AssertionError: argument is not an integer')
    exit()

if int(sys.argv[1]) % 2 == 0:
    print('I\'m Even.')
else:
    print('I\'m Odd.')

