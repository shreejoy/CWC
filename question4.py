import sys


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

# Ask input and raise error if int coversion fails
try:
    DAY = int(input("Enter day (int) of your date > "))
    MONTH = int(input("Enter month (int) of your date > "))
    YEAR = int(input("Enter year (int) of your date > "))
except Exception as e:
    print(e)
    sys.exit("Program Aborted!")

# Test leap year and assign the days list
DMY = DMLY if test_leap_year(YEAR) else DMNLY

# Number of days > 31 not possible, Same for number of years > 12
if DAY > 31 or MONTH > 12:
    sys.exit("Invalid date inserted")

# Calculation for number of days
NDAYS += DAY
for i in range(0, MONTH):
    NDAYS += DMY[i]

# Print result
print(f"The number of days for date {DAY}/{MONTH}/{YEAR} is {NDAYS} days")
