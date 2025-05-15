# Program to calculate the sum of odd numbers divisible by 5 from 1 to 100
# Loops through numbers 1 to 100, checks for odd and divisibility by 5, and sums them

# Initialize sum
sum_odd_div5 = 0

# Loop through numbers from 1 to 100
for i in range(1, 101):
    if i % 2 == 1 and i % 5 == 0:  # Check if odd and divisible by 5
        sum_odd_div5 += i

# Print the result
print(f"Sum of odd numbers divisible by 5 from 1 to 100: {sum_odd_div5}")
