# Program to calculate GST (Goods and Services Tax)

# Function to calculate GST amount and total price
def calculate_gst(original_price, gst_rate):
    """Calculate GST amount and total price."""
    gst_amount = (original_price * gst_rate) / 100  # Calculate GST amount
    total_price = original_price + gst_amount       # Calculate total price after GST
    return gst_amount, total_price

try:
    # Take user input for original price and GST rate
    original_price = float(input("Enter the original price: "))
    gst_rate = float(input("Enter the GST rate (%): "))
    # Calculate GST and total price
    gst_amount, total_price = calculate_gst(original_price, gst_rate)
    # Print the results formatted to two decimal places
    print(f"GST amount: {gst_amount:.2f}")
    print(f"Total price after GST: {total_price:.2f}")
except ValueError:
    # Handle invalid input
    print("Invalid input. Please enter numeric values.")
