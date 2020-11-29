import sys

COUNTER = 0
X = int(input("X > "))
Y = int(input("Y > "))
A = int(input("A > "))
B = int(input("B > "))
N = int(input("N > "))


for COUNTER != N:
    if (X - A + Y - B) < N:
        break

    if X <= A and Y <= B:
        print('e2')
        break

    if X > A:
        N += 1
        print('e3')
        X -= 1
        print('X n A', X, A)

    if Y > B:
        N += 1
        print('e4')
        Y -= 1
        print('Y n B', Y, B)

print(X - Y, 'answer')
