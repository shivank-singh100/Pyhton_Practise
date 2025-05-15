# Program to check if a character is an alphabet or not
# Takes user input and prints whether it is an alphabet character

# Get input from the user
char = input("Enter a character: ")

# Check if the input is a single character and is an alphabet letter
if len(char) == 1 and char.isalpha():
    print(f"{char} is an alphabet.")  # If true, print that it is an alphabet
else:
    print(f"{char} is not an alphabet.")  # Otherwise, print that it is not an alphabet
