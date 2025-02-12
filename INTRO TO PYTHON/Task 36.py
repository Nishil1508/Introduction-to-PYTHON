# Write a Python script to check if a given key already exists in a dictionary

my_dict = {'a': 1, 'b': 2, 'c': 3}

def check_key_existence(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False

key_to_check = 'b'

if check_key_existence(my_dict, key_to_check):
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")
