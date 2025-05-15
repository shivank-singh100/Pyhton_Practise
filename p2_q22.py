# Program to print the ASCII codes of each character in a message
# Takes a message as input and prints the ASCII code for each character

# Get input message from the user
message = input("Enter a message: ")

# Print ASCII codes for each character in the message
print("ASCII codes:")
for ch in message:
    print(f"{ch}: {ord(ch)}")
