# reverse the values
num1 = 0
num2 = 0
final = 0

# get the reverse of number


def reverse(num):
    rev = 0
    while (num >= 1):
        n = num % 10
        rev = (10 * rev) + n
        num = num // 10
    return rev


# loop i and j to find the solution
for i in range(100, 1000):
    for j in range(100, 1000):
        p = i * j
        r = reverse(p)

        if p == r:
            num1 = i
            num2 = j
            final = p

# print the result
print(
    f"The largest palindrome number made from the product of two 3-digit numbers is {final}. It is the product of {num1} and {num2}.")
