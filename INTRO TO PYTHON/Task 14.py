#Write a Python program to add 'in' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then 
#add 'ly' instead if the string length of the given string is less than 3, leave it unchanged


def modify_string(s):
    if len(s) < 3:
        return s  # Leave unchanged if length is less than 3
    elif s.endswith("ing"):
        return s + "ly"  # Add 'ly' if string already ends with 'ing'
    else:
        return s + "ing"  # Add 'ing' otherwise

# Get user input
string = input("Enter a string: ")

# Get and print the modified string
result = modify_string(string)
print("Modified string:", result)
