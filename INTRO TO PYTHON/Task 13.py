# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
def swap_and_combine(str1, str2):
    # Swap the first two characters of each string
    str1_swapped = str2[:2] + str1[2:]
    str2_swapped = str1[:2] + str2[2:]
    
    # Combine the two strings with a space
    return str1_swapped + " " + str2_swapped

# Get user input
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Get the result after swapping and combining
result = swap_and_combine(str1, str2)
print("Result:", result)
