#Write a Python script to sort (ascending and descending) a dictionary by value. 

my_dict = {1: 50, 2: 30, 3: 20, 4: 40}


ascending_sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

descending_sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Dictionary sorted by value in ascending order:", ascending_sorted_dict)
print("Dictionary sorted by value in descending order:", descending_sorted_dict)
