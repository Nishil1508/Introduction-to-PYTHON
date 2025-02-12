#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return 
#instead of the empty string


def first_last_chars(s):
    if len(s) < 2:
        return ""  # Return empty string if length is less than 2
    return s[:2] + s[-2:]  # Concatenate first 2 and last 2 characters

# Get user input
string = input("Enter a string: ")

# Get and print the result
result = first_last_chars(string)
print("Result:", result)
