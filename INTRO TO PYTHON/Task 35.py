# Write a Python script to concatenate following dictionaries to create a new one. 


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

merged_dict = {**dict1, **dict2, **dict3}

print("Merged dictionary:", merged_dict)
