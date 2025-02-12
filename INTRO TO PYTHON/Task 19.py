#Write a Python program to count the number of strings where the string  length is 2 or more and the first and last character are same from a given list 
#of strings.

def count_special_strings(strings):
    count = 0
    for s in strings:
        if len(s) >= 2 and s[0] == s[-1]:  # Check length and first-last character
            count += 1
    return count

strings = input("Enter words separated by spaces: ").split()

result = count_special_strings(strings)
print(f"Count of matching strings: {result}")
