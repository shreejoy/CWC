# take input of the first string 
str1 = input("Enter the first string > ")
# take input of the second string
str2 = input("Enter the second string > ")
# sort the second string and remove duplicates
str2 = sorted(set(str2))
# remove the sorted characters of str2 from st2
for s in str2:
    # lowercase
    str1 = str1.replace(s.lower(), '')
    # uppercase
    str1 = str1.replace(s.upper(), '')
# print the result
print("The final string is >", str1)
