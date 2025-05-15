# Program to print the sum of the series: 1^3 + 2^3 + 3^3 + ... + n^3
# Takes n as input and prints the sum of cubes from 1 to n

# Get input from the user
n = int(input("Enter the value of n: "))

# Calculate the sum of cubes using a loop
sum_cubes = 0
for i in range(1, n + 1):
    sum_cubes += i ** 3

# Print the result
print(f"Sum of the series 1^3 + 2^3 + ... + {n}^3 is: {sum_cubes}")
