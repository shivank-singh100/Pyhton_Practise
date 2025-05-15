# Program to print the factors of a given number
# Takes a number as input and prints all its factors

# Get input from the user
num = int(input("Enter a number: "))

# Print all factors of the number
print(f"Factors of {num} are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
