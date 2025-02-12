#Write a Python function to reverses a string if its length is a multiple # Function to reverse the string if its length is a multiple of 4


def reverse_if_multiple_of_4(s):
    if len(s) % 4 == 0:
        return s[::-1]  # Reverse the string
    else:
        return s  # Return unchanged if length is not a multiple of 4

# Get user input
string = input("Enter a string: ")

# Get and print the result
result = reverse_if_multiple_of_4(string)
print("Result:", result)
