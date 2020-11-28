import sys

try:
    # Get the input and convert to int
    N = int(input("Enter size of matrix > "))
    # Get the range
    RANGE = range(N)
except:
    # If exception raise then exit
    sys.exit("The entered value should be in integer.")

# Create a placeholder N x N matrix with all 0 as element
MATRIX = [[0 for i in RANGE] for i in RANGE]

# Update the values of [i][N - i - 1] to 1
for i in range(N):
    MATRIX[i][N - i - 1] = 1

# Update the value of [i][i] to 1
for i in RANGE:
    MATRIX[i][i] = 1

# If N is an odd number then update the value [N / 2][0] and [0][N / 2] to 1
if (N % 2 != 0):
    A = N // 2
    MATRIX[A][0] = 1
    MATRIX[0][A] = 1

# Print the matrix
for i in RANGE:
    for j in RANGE:
        print(MATRIX[i][j], end=" ")
    # create a new line
    print("")
