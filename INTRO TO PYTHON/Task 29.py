#Write a Python program to check whether a list contains a sub list 
def contains_sublist(main_list, sublist):

    str_main_list = ''.join(map(str, main_list))
    str_sublist = ''.join(map(str, sublist))
    
    
    return str_sublist in str_main_list

main_list = [1, 2, 3, 4, 5]
sublist = [3, 4]

result = contains_sublist(main_list, sublist)

if result:
    print(f"The list contains the sublist {sublist}.")
else:
    print(f"The list does not contain the sublist {sublist}.")


