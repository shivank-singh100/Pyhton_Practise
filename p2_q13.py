# Program to find the largest digit of a given number
# Takes a number as input and prints the largest digit

# Get input from the user
num = input("Enter a number: ")

# Extract digits and find the largest one
largest_digit = max([int(ch) for ch in num if ch.isdigit()])

# Print the result
print(f"Largest digit: {largest_digit}")
