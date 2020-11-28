import sys

# List of vowels
VOWELS = ['A', 'E', 'I', 'O', 'U']
# Get the input
string = input("Enter your string >")

# If any character of the given input is not a alphabet the exit
check = [C.isalpha() for C in list(string)]
if False in check:
    sys.exit('Invalid input')

nstring = ''.join([i for i in string if i.upper() not in VOWELS])

if nstring == string:
    raise Exception('The string consists of no vowels.')
else:
    print(nstring)
