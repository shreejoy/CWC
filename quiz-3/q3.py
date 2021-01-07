ROMAN_NUM = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
}

roman_val = ''
num = int(input("Enter your desired number > "))

if num < 1 or num > 3999:
    sys.exit('Cannot find the roman numeral for the given input.')

for roman in ROMAN_NUM.keys():
    while num >= roman:
        roman_val += ROMAN_NUM[roman]
        num -= roman

print(f"The roman numeral for {num} is {roman_val}")
