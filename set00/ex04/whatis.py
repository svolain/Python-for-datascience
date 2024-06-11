import sys

try:
    assert len(sys.argv) == 2, 'AssertionError: more than one argument is provided'
    assert sys.argv[1].lstrip("-").isnumeric() == True, 'AssertionError: argument is not an integer'
except AssertionError as msg:
    print(msg)
    exit(1)
if int(sys.argv[1]) % 2 == 0:
    print('I\'m Even.')
else:
    print('I\'m Odd.')

