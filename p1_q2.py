# This program calculates the total number of seconds in a given year,
# taking into account whether the year is a leap year or not.

# Take year as input from the user
year = int(input("Enter a year: "))

# Function to check if a year is a leap year
# A leap year is divisible by 4, but not by 100 unless also divisible by 400
# Example: 2000 is a leap year, 1900 is not
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Determine the number of days in the year
if is_leap_year(year):
    days = 366  # Leap year
else:
    days = 365  # Non-leap year

# Calculate total seconds in the year
seconds_in_a_year = days * 24 * 60 * 60

# Print the result
print(f"Total number of seconds in the year {year}: {seconds_in_a_year}")