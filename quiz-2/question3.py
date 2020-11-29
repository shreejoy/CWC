X = input("X > ")
Y = input("Y > ")
A = input("A > ")
B = input("B > ")
N = input("N > ")

for i in range(N):
    if X <= A and Y <= B:
        break

    if X > A:
        X -= 1

    if Y > Y:
        Y -= 1
