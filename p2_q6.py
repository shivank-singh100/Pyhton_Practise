# Program to convert kilometers to miles
# Takes user input in kilometers and prints the equivalent in miles

try:
    km = float(input("Enter distance in kilometers: "))  # Input distance in kilometers
    miles = km * 0.621371  # Conversion factor
    print(f"{km} kilometers is equal to {miles:.2f} miles.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")