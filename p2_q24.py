# Program to print every integer between 1 and n divisible by m
# Also reports whether each such number is even or odd

# Get input from the user
n = int(input("Enter the value of n: "))  # Upper limit
m = int(input("Enter the value of m: "))  # Divisor

# Print header
print(f"Numbers between 1 and {n} divisible by {m} (with even/odd report):")

# Loop through numbers from 1 to n
for i in range(1, n + 1):
    if i % m == 0:  # Check if i is divisible by m
        kind = "even" if i % 2 == 0 else "odd"  # Determine if i is even or odd
        print(f"{i} is divisible by {m} and is {kind}")  # Print result
