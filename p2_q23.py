# Program to print the first ten Mersenne numbers
# A Mersenne number is of the form 2^n - 1

for n in range(1, 11):
    mersenne = 2 ** n - 1
    print(f"Mersenne number {n}: {mersenne}")
