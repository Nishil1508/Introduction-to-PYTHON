#Write a python program to sum of the first n positive integers.



def sum_of_integers(n):
    return n * (n + 1) // 2  # Formula for sum of first n positive integers

# Get user input
n = int(input("Enter a number: "))

# Calculate and print the result
result = sum_of_integers(n)
print(f"The sum of the first {n} positive integers is: {result}")
