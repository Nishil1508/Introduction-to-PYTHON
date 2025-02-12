#Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

# Function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

# Get user input
num = int(input("Enter a number: "))
check_even_odd(num)
