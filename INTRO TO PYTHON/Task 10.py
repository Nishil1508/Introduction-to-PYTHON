#Write a Python program to count the number of characters (character frequency) in a string 


def char_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# Get user input
string = input("Enter a string: ")

# Calculate and print the character frequencies
result = char_frequency(string)
print("Character frequencies:", result)
