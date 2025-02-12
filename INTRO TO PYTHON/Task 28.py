#Write a Python program to get unique values from a list 

def get_unique_values(lst):
    
    unique_values = list(set(lst))
    return unique_values


my_list = [1, 2, 2, 3, 4, 4, 5]
result = get_unique_values(my_list)

print(f"The unique values are: {result}")
