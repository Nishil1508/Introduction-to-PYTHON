# Write a Python program to check a list is empty or not


def is_list_empty(lst):
    return len(lst) == 0  

numbers = input("Enter numbers separated by spaces (leave empty for an empty list): ").split()

numbers = list(map(int, numbers)) if numbers else []

if is_list_empty(numbers):
    print("The list is empty.")
else:
    print("The list is not empty.")
