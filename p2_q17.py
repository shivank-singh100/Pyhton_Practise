# Program to convert a binary number to decimal
# Takes a binary number as input and prints its decimal representation

# Get input from the user
binary = input("Enter a binary number: ")

try:
    # Convert binary string to decimal integer using int() with base 2
    decimal = int(binary, 2)
    # Print the decimal representation
    print(f"Decimal representation: {decimal}")
except ValueError:
    # Handle invalid input (non-binary characters)
    print("Invalid input. Please enter a valid binary number.")
