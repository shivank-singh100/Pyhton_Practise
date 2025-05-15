# Program to print the frequency of digits present in a number
# Takes a number as input and prints the frequency of each digit (0-9)

# Get input from the user
num = input("Enter a number: ")

# Initialize a dictionary to store digit frequencies (keys: '0'-'9', values: 0)
freq = {str(d): 0 for d in range(10)}

# Loop through each character in the input string
for ch in num:
    if ch.isdigit():  # Check if the character is a digit
        freq[ch] += 1  # Increment the count for that digit

# Print the frequency of each digit from 0 to 9
print("Digit frequencies:")
for d in range(10):
    print(f"{d}: {freq[str(d)]}")
