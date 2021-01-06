str1 = input("Enter the first string > ")
str2 = input("Enter the second string > ")

str2 = sorted(set(str2))

for s in str2:
    str1 = str1.replace(s.lower(), '')
    str1 = str1.replace(s.upper(), '')

print(str1)
