import sys

X = int(input("X > "))
Y = int(input("Y > "))
A = int(input("A > "))
B = int(input("B > "))
N = int(input("N > "))

if (X - A + Y - B) < N:
    sys.exit('e1')

for i in range(N):
    if X <= A and Y <= B:
        print('e2')
        break

    if X > A:
        print('e3')
        X -= 1
        print('X n A', X, A)

    if Y > B:
        print('e4')
        Y -= 1
        print('Y n B', Y, B)

print(X - Y, 'answer')
