# Program to count uppercase and lowercase characters in a string
# Takes a string as input and prints the counts of uppercase and lowercase letters

# Get input string from the user
s = input("Enter a string: ")

# Initialize counters for uppercase and lowercase letters
upper_count = 0  # Counter for uppercase characters
lower_count = 0  # Counter for lowercase characters

# Iterate through each character in the string
for char in s:
    if char.isupper():
        upper_count += 1  # Increment if character is uppercase
    elif char.islower():
        lower_count += 1  # Increment if character is lowercase

# Print the results
print(f"Uppercase characters: {upper_count}")
print(f"Lowercase characters: {lower_count}")
