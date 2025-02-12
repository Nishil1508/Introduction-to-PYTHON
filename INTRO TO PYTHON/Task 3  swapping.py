# Using a temp variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp = a
a = b
b = temp

print(f"After swapping: a = {a}, b = {b}")

# Without using a temp variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a  # Python tuple unpacking

print(f"After swapping: a = {a}, b = {b}")
