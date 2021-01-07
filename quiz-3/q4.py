rc = int(input("Enter the number of rows > "))
max_num = rc // 2 + 1

def get_pattern(n, s):
    pattern = ' ' * s

    while n > 1:
        pattern += str(n)
        n -= 1

    pattern = pattern + '1' + pattern[::-1]
    return pattern

p = []
for j in range(max_num):
    spaces = (rc - max_num - j)
    p.append(get_pattern(j + 1, spaces))

p = p + p[0:(max_num - 1)][::-1]

for q in p:
    print(q)
