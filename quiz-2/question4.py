N = int(input("Enter size of matrix > "))
MATRIX = mat = [[0 for i in range(N)] for i in range(N)]

for i in range(N):
    MATRIX[i][i] = 1

for i in range(N):
    MATRIX[i][N - i - 1] = 1

if (N % 2 != 0):
    MATRIX[N // 2][0] = 1
    MATRIX[0][N // 2] = 1

for i in range(N):
    for j in range(N):
        print(MATRIX[i][j], end=" ")
    print("")
