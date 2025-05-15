# Program to convert a decimal number to binary
# Takes a decimal number as input and prints its binary representation

# Get input from the user
decimal = int(input("Enter a decimal number: "))

# Convert decimal to binary using bin(), remove '0b' prefix
binary = bin(decimal)[2:]

# Print the result
print(f"Binary representation: {binary}")
