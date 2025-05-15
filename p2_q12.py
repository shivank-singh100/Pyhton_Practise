# Program to count the number of digits in a given number
# Takes a number as input and prints the count of its digits

# Get input from the user
num = input("Enter a number: ")

# Count the number of digits (excluding any sign or decimal point)
digit_count = len([ch for ch in num if ch.isdigit()])

# Print the result
print(f"Number of digits: {digit_count}")