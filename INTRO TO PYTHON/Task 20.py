#Write a Python program to remove duplicates from a list. 

def remove_duplicates(lst):
    return list(set(lst))  # Convert list to set to remove duplicates, then back to list

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique_numbers = remove_duplicates(numbers)
print("List after removing duplicates:", unique_numbers)
