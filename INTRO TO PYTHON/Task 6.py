# Function to calculate sum with the given condition
def sum_integers(a, b, c):
    if a == b or b == c or a == c:
        return 0
    else:
        return a + b + c

# Get user input
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

# Calculate and print the result
result = sum_integers(a, b, c)
print(f"The result is: {result}")
