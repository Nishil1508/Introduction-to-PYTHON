#Write a Python program to create a dictionary from a string. Note: Track the count of the letters from the string.

input_string = "hello world"

letter_count = {}


for letter in input_string:

    if letter.isalpha():
        if letter in letter_count:
        
            letter_count[letter] += 1
        else:
        
            letter_count[letter] = 1

print("Letter count dictionary:", letter_count)
