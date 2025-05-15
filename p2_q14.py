# Program to find the difference between the greatest and smallest digit in a number
# Takes a number as input and prints the difference between its largest and smallest digit

# Get input from the user
num = input("Enter a number: ")

# Extract digits from the input
digits = [int(ch) for ch in num if ch.isdigit()]

# Find the difference between the largest and smallest digit
diff = max(digits) - min(digits)

# Print the result
print(f"Difference between greatest and smallest digit: {diff}")
