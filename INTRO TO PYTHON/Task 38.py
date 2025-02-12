#Write a Python program to check multiple keys exists in a dictionary


my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


def check_multiple_keys_existence(dictionary, keys):
    return all(key in dictionary for key in keys)

keys_to_check = ['a', 'b', 'e']

if check_multiple_keys_existence(my_dict, keys_to_check):
    print(f"All keys {keys_to_check} exist in the dictionary.")
else:
    print(f"Not all keys {keys_to_check} exist in the dictionary.")
