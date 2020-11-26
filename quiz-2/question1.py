VOWELS = ['A', 'E', 'I', 'O', 'U']
string = input("Enter your string >")

try:
    string = float(string)
except:
    pass

try:
    string = int(string)
except:
    pass

if isinstance(string, int):
    raise Exception('Invalid input')

nstring = ''.join([i for i in string if i.upper() not in VOWELS])

if nstring == string:
    raise Exception('The string consists of no vowels.')
else:
    print(nstring)

