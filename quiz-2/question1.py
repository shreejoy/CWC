VOWELS = ['A', 'E', 'I', 'O', 'U']
string = input("Enter your string >")

try:
  string = float(string)
except:
  pass

try:
  string = int(string)
except:
  pass

if isinstance(string, int):
  return 'Invalid input'
