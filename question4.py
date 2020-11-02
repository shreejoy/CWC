import sys


# test for leap year and return value accordingly
def test_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# Number of days
NDAYS = 0

# Day's in Month's of Non Leap Year
DMNLY = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Day's in Month's of Leap Year
DMLY = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

MONTHS = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12
}

# Ask input and raise error if int coversion fails
print("Enter your date refering to the below given example format.")
print("1st January 2020")
DATE = input("> ")

try:
    DATE = DATE.split(" ")
    DAY = int(DATE[0][:-2])
    MONTH = int(MONTHS[DATE[1].lower()])
    YEAR = int(DATE[2])
except Exception as e:
    sys.exit(f"Program Aborted: {e}")

# Test leap year and assign the days list
DMY = DMLY if test_leap_year(YEAR) else DMNLY

# Number of days > 31 not possible, Same for number of years > 12
if DAY > 31 or MONTH > 12:
    sys.exit("Invalid date inserted")

# Calculation for number of days
NDAYS += DAY
for i in range(0, MONTH - 1):
    NDAYS += DMY[i]

# Print result
print(f"The number of days for date {DAY}/{MONTH}/{YEAR} is {NDAYS} days")
