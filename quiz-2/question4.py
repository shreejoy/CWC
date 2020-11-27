N = input("Enter size of matrix > ")
MATRIX = mat = [[0 for i in range(N)] for i in range(N)]

for i in range(N):
        mat[i][i] = 1
    for i in range(N):
        mat[i][N - i - 1] = 1
    if (N % 2 != 0):
        mat[N // 2][0] = 1
        mat[0][N // 2] = 1
    for i in range(N):
        for j in range(N):
            print(mat[i][j], end = " ")
             
        print()
