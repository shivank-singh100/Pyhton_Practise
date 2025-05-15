# Program to check if a given number is composite
# Takes a number as input and prints whether it is composite or not

# Get input from the user
num = int(input("Enter a number: "))

# A composite number has more than two factors (not 1 and not prime)
if num > 1:
    # Check for factors other than 1 and itself
    for i in range(2, num):
        if num % i == 0:
            # If a factor is found, the number is composite
            print(f"{num} is a composite number.")
            break
    else:
        # If no factors are found, the number is not composite (it's prime)
        print(f"{num} is not a composite number.")
else:
    # Numbers less than or equal to 1 are not composite
    print(f"{num} is not a composite number.")
