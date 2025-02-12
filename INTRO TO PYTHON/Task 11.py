# Write a Python program to count occurrences of a substring in a string. 


def count_substring_occurrences(string, substring):
    return string.count(substring)

# Get user input
string = input("Enter a string: ")
substring = input("Enter the substring to search for: ")

# Calculate and print the occurrences of the substring
result = count_substring_occurrences(string, substring)
print(f"The substring '{substring}' appears {result} time(s) in the string.")


