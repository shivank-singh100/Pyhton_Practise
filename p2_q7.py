# Program to display a menu to calculate area of square or rectangle
# User selects the shape and enters dimensions; program prints the area

# Display menu options
print("Menu:")
print("1. Area of Square")
print("2. Area of Rectangle")

# Get user's choice
choice = input("Enter your choice (1 or 2): ")

try:
    if choice == '1':
        # Area of square: side * side
        side = float(input("Enter the side of the square: "))
        area = side * side
        print(f"Area of square: {area}")
    elif choice == '2':
        # Area of rectangle: length * width
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print(f"Area of rectangle: {area}")
    else:
        # Handle invalid menu choice
        print("Invalid choice. Please enter 1 or 2.")
except ValueError:
    # Handle invalid numeric input
    print("Invalid input. Please enter numeric values.")