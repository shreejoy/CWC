import sys
# take the input of an odd number
num = int(input("Enter the number (odd) > "))
# only odd numbers are accepted
if num % 2 == 0:
    sys.exit("Only odd numbers are accepted")

# get the range of numbers
r = num // 2 + 1

# function to generate pattern


def genp(n, s):
    p = ' ' * s

    while n > 1:
        p += str(n)
        n -= 1

    p = p + '1' + p[::-1]
    return p


# placeholder
pattern = []

# assign the max range and the needed spaces
for i in range(r):
    spaces = (num - r - i)
    pattern.append(genp(i + 1, spaces))

# join the pattern with 1 and its reverse respectively
pattern += pattern[:-1][::-1]

# print the pattern
for p in pattern:
    print(p)
