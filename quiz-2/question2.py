import sys

"""
variable TMO represents temprature of the room in degree C
variable NDO represents the number of times the door was opened
variable RT represents the time for which purifier was operational.
variable EFF represents the effieceny changed due to room temprature
"""

# get the needed values and convert to int
try:
    RT = int(input("Purifier's working time (minutes) > "))
    NDO = int(input("Count of times door opened (int) > "))
    TMP = int(input("Temperature of room in degree (C) > "))
except Exception as e:
    print(f"Invalid input: {e}")


"""
The door can be opened once a minute so its not possible to have the amount of running duration to be 
numerically less than the number of times the door was opened.
"""
if NDO > RT:
    raise sys.exit(
        "Not a possible scenario. Please try again with correct inputs")


# Calculate the effect on efficency on purifier due to the the
EFF = int((TMP - 25) * 2)
# Calculate the required value
total = (RT - NDO) * (40 + EFF) + NDO * (30 + EFF)

# If the value is 0 or less then it mean the purifier failed to do any work.
if total <= 0:
    sys.exit("Under the given sitution the purifier will not work at all")
else:
    print(f"The total amount purfied is {total}")
