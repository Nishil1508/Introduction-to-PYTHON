#Write a Python program to split a list into different variables.
def split_list_into_variables(lst):
    
    if len(lst) >= 3:  
        var1, var2, var3 = lst[0], lst[1], lst[2]
        return var1, var2, var3
    else:
        return "List doesn't have enough elements to split."

my_list = [10, 20, 30]
var1, var2, var3 = split_list_into_variables(my_list)

print(f"Variable 1: {var1}")
print(f"Variable 2: {var2}")
print(f"Variable 3: {var3}")
