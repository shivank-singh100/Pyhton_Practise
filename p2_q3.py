# Program to print a single digit number and its next two consecutive numbers
# Takes user input and handles invalid input gracefully

try:
    n = int(input("Enter a single digit number: "))  # Take integer input from user
    # Print the number and its next two consecutive numbers
    print(f"{n}, {n+1}, {n+2}")
except ValueError:
    # Handle invalid input (non-integer)
    print("Invalid Value")