# Program to calculate compound interest
# Takes principal, rate, time, and number of times interest applied per year as input

try:
    # Get user input for principal amount, interest rate, time, and compounding frequency
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    time = float(input("Enter the time (in years): "))
    n = int(input("Enter the number of times interest is compounded per year: "))
    
    # Calculate total amount using the compound interest formula
    # Formula: A = P * (1 + r/n)^(n*t)
    amount = principal * (1 + rate/(100*n))**(n*time)
    
    # Calculate compound interest earned
    compound_interest = amount - principal
    
    # Print the results, formatted to two decimal places
    print(f"Compound Interest: {compound_interest:.2f}")
    print(f"Total Amount: {amount:.2f}")
except ValueError:
    # Handle invalid input (non-numeric values)
    print("Invalid input. Please enter numeric values.")