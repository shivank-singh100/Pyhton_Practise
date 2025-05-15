# Program to check if a given year is a leap year or not
# Takes user input for the year and prints whether it is a leap year

# Get year input from the user
year = int(input("Enter a year: "))

# Check leap year condition using Gregorian calendar rules
# A year is a leap year if:
# - It is divisible by 4, but not by 100
# - OR it is divisible by 400
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
