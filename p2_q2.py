# Program to print a number, its XOR with 2, and its XOR with 3
# Takes user input and handles invalid input gracefully

try:
    n = int(input("Enter a number: "))  # Take integer input from user
    # Print the number, its XOR with 2, and its XOR with 3
    print(f"{n} {n^2} {n^3}")
except ValueError:
    # Handle invalid input (non-integer)
    print("Invalid Value.")