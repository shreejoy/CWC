ROMAN_NUM = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX'
    10: 'X',
    40: 'XL',
    50: 'L',
    100: 'C',
    400: 'CD'
    500: 'D',
    900: 'CM'
    1000: 'M'
}

num = int(input("Enter your desired number > "))

i = 0
roman_val = ''

while  num > 0:
    for _ in range(num // val[i]):
        roman_val += syb[i]
        num -= val[i]
    i += 1
