# Program to print the first ten terms of the series: s = 1/a + 1/a^2 + 1/a^3 + ... + 1/a^n
# Takes input for 'a' and prints the first ten terms

a = float(input("Enter the value of a: "))

print("First ten terms of the series:")
for n in range(1, 11):
    term = 1 / (a ** n)
    print(f"1/{a}^{n} = {term}")
