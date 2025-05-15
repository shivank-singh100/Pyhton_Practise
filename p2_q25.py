# Program to check if a given number is a perfect number or not
# A perfect number is a number that is equal to the sum of its proper divisors (excluding itself)

# Get input from the user
num = int(input("Enter a number: "))

# Calculate the sum of proper divisors
sum_divisors = 0
for i in range(1, num):
    if num % i == 0:
        sum_divisors += i

# Check if the number is perfect
if sum_divisors == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
    # Show an example of a perfect number
    print("Example: 28 is a perfect number because 1 + 2 + 4 + 7 + 14 = 28.")
