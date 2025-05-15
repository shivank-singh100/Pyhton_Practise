# Program to check if a two-digit number is a Special Number
num = input("Enter a double digit number: ")
# Check if the sum and product of the digits add up to the original number
# Special Number: (sum of digits + product of digits) == original number
print(
    "This is a Special Number."
    if int(num) == sum(map(int, num)) + int(num[0]) * int(num[1])
    else "This is a Normal Number."
)