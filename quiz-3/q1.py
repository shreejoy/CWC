import sys

arr = []
arr_len = int(input("Enter the length of the list (more than 3) > "))

if arr_len > 3:
    print("Great! Now enter the elements of the list")
else:
    sys.exit("The length of the list cannot be less than 3")

for i in range(arr_len):
    num = input("> ")
    if num.isnumeric():
        arr.append(int(num))
    else:
        sys.exit("The given input should be an integer.")

csum = int(input("Enter your desired sum > "))

if csum > sum(arr):
    sys.exit("(1) No triplet in the given array can satisfy the given sum.")

triplets = [[i, j, k]
            for i in range(0, arr_len - 2)
            for j in range(i + 1, arr_len - 1)
            for k in range(j + 1, arr_len)
            if arr[i] + arr[j] + arr[k] == csum]

if not triplets:
    sys.exit("(2) No triplet in the given array can satisfy the given sum.")

print(f"A total of {len(triplets)} triplet(s) is/are found in the given list.")
for triplet in triplets:
    print("> ", triplet)
