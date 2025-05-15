# Program to calculate the result of the expression: (4*x^4) + (3*y^3) + (9*z^2) + 6*3.14
# Takes user input for x, y, and z, then prints the result

# Get input values from the user
x = int(input("Enter the value of X: "))  # Input for x
y = int(input("Enter the value of Y: "))  # Input for y
z = int(input("Enter the value of Z: "))  # Input for z

# Calculate the result using the given formula
# 4*x^4 + 3*y^3 + 9*z^2 + 6*3.14
res = (4 * x ** 4) + (3 * y ** 3) + (9 * z ** 2) + 6 * 3.14

# Print the result
print(f"Result: {res}")