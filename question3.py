# reserved values
MAX_LENGTH = 0
FINAL_NUMBER = 0

# loop to get the answer
for i in range(2, 1000000):
    LENGTH = 1
    NUMBER = i

    # this is a time taking program. Keep user notified periodically
    if (NUMBER % 100000 == 0):
        print(f"Completed number test for {NUMBER/1000000} million numbers.")

    # verify the check
    while i > 1:
        if i % 2 == 0:
            i = i/2
        else:
            i = (3 * i) + 1
        LENGTH += 1

    # if case True then update max values
    if LENGTH > MAX_LENGTH:
        MAX_LENGTH = LENGTH
        FINAL_NUMBER = NUMBER

# print final answer
print(f"{FINAL_NUMBER} generates the largest chain of number for collatz law. The length of chain is {MAX_LENGTH}")
