import sys

# generate placeholder list
arr = []
# get the length of the list
arr_len = int(input("Enter the length of the list (more than 3) > "))

# if length less than 3 then abort program
if arr_len > 3:
    print("Great! Now enter the elements of the list")
else:
    sys.exit("The length of the list cannot be less than 3")

# Take input of list items
for i in range(arr_len):
    num = input("> ")
    # if the input is not an number then abort program
    if num.isnumeric():
        arr.append(int(num))
    else:
        sys.exit("The given input should be an integer.")

# Take input of desired sum
csum = int(input("Enter your desired sum > "))

# if the sum of entire list cannot match the desired sum then no possible triplet exists
if csum > sum(arr):
    sys.exit("(1) No triplet in the given array can satisfy the given sum.")

# get the list of triplets
triplets = [[str(arr[i]), str(arr[j]), str(arr[k])]
            for i in range(0, arr_len - 2)
            for j in range(i + 1, arr_len - 1)
            for k in range(j + 1, arr_len)
            if arr[i] + arr[j] + arr[k] == csum]

# abort program if no triplet exists
if not triplets:
    sys.exit("(2) No triplet in the given array can satisfy the given sum.")

# print all the triplets
print(f"A total of {len(triplets)} triplet(s) is/are found in the given list.")
for triplet in triplets:
    print("> ", ', '.join(triplet))
