import sys

# Reserved variable to be used later.
OUTPUT = ""

# take input and convert them to list of characters.
INPUT = list(input("Enter the DNA strand: "))

# python dict for complements.
COMPLEMENT = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U"
}

# Loop the list of characters and build the output.
for I in INPUT:
    try:
        OUTPUT += COMPLEMENT[I]
    except:
        OUTPUT = 'invalid'
        break

# If the output is invalid the report user about the error. Else print the output.
if OUTPUT == 'invalid':
    sys.exit("Invalid Input.")
else:
    print("Your OUTPUT is >", OUTPUT)
