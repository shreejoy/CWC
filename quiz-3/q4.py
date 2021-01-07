num = int(input("Enter the number (odd) > "))
r = num // 2 + 1


def genp(n, s):
    p = ' ' * s

    while n > 1:
        p += str(n)
        n -= 1

    p = p + '1' + p[::-1]
    return p


pattern = []
for i in range(r):
    spaces = (num - r - i)
    pattern.append(genp(i + 1, spaces))

pattern += pattern[:-1][::-1]

for p in pattern:
    print(p)
