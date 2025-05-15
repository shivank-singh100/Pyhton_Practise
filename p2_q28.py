# Program to print the first n perfect numbers
# A perfect number is a number that is equal to the sum of its proper divisors (excluding itself)

def is_perfect(num):
    """
    Check if a number is perfect.
    A perfect number is equal to the sum of its proper divisors.
    Example: 28 -> 1 + 2 + 4 + 7 + 14 = 28
    """
    # Calculate the sum of all divisors of num except itself
    divisor_sum = sum(i for i in range(1, num) if num % i == 0)
    return num == divisor_sum

# Get the number of perfect numbers to print from the user
n = int(input("Enter how many perfect numbers to print: "))
count = 0  # Counter for perfect numbers found
num = 2    # Start checking from 2 (smallest perfect number is 6)

print(f"First {n} perfect numbers:")
while count < n:
    if is_perfect(num):
        print(num)
        count += 1
    num += 1
