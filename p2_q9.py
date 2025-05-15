# Program to compute the result of an expression entered by the user using eval()
# Allows the user to enter a full mathematical expression (e.g., 5 + 3, 10 * 2, 2 ** 3)

try:
    # Prompt the user to enter a mathematical expression
    expr = input("Enter an expression (e.g., 5 + 3): ")
    # Evaluate the expression using eval()
    result = eval(expr)
    # Print the result
    print(f"Result: {result}")
except Exception:
    # Handle any errors (invalid input, invalid operation, etc.)
    print("Invalid input or operation.")