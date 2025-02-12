#Write a Python program to find the highest 3 values in a dictionary

my_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}

top_3_values = sorted(my_dict.values(), reverse=True)[:3]

top_3_keys = [key for key, value in my_dict.items() if value in top_3_values]

print("Top 3 values:", top_3_values)
print("Keys corresponding to the top 3 values:", top_3_keys)
