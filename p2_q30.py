# Program to print all prime numbers between a given range
# Takes two numbers as input and prints all primes in that range

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Get the range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(f"Prime numbers between {start} and {end}:")
for n in range(start, end + 1):
    if is_prime(n):
        print(n)
