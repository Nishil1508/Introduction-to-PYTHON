#Write a Python function that takes two lists and returns true if they have at least one common member. 


def has_common_member(list1, list2):
    return bool(set(list1) & set(list2)) 

list1 = list(map(int, input("Enter first list of numbers: ").split()))
list2 = list(map(int, input("Enter second list of numbers: ").split()))

if has_common_member(list1, list2):
    print("The lists have at least one common element.")
else:
    print("The lists have no common elements.")
