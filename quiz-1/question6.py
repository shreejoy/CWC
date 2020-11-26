# reserve values
count = 0
num = 2


# check prime number
def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

# iterate till we get the solution
print("Getting you the 10001 th prime number. It may take upto 1min, Please be paitent.")
while count < 10002:
    count += 1 if is_prime(num) else 0
    num += 1

# print the results
print(f"The 10001th prime number is {num - 1}")
