#Write a Python program to test whether a passed letter is a vowel or not.

# Function to check if a letter is a vowel
def check_vowel(letter):
    vowels = "aeiouAEIOU"  # Including both lowercase and uppercase vowels
    if letter in vowels:
        print(f"{letter} is a vowel.")
    else:
        print(f"{letter} is not a vowel.")

# Get user input
letter = input("Enter a letter: ")

# Ensure input is a single letter
if len(letter) == 1 and letter.isalpha():
    check_vowel(letter)
else:
    print("Please enter a valid letter.")
