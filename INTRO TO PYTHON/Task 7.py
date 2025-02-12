#Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5


def check_condition(a, b):
    if a == b or a + b == 5 or abs(a - b) == 5:
        return True
    else:
        return False

# Get user input
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

# Check the condition and print the result
result = check_condition(a, b)
print("Result:", result)
