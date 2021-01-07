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

num = int(input("Enter your desired number > "))

i = 0
roman_val = ''

while num > 0:
    for _ in range(num // val[i]):
        roman_val += syb[i]
        num -= val[i]
    i += 1
