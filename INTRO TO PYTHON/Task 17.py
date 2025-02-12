#  Write a Python function to insert a string in the middle of a string. 
   

def insert_middle(original, insert):
    middle = len(original) // 2  # Find the middle index
    return original[:middle] + insert + original[middle:]

original_string = input("Enter the original string: ")
insert_string = input("Enter the string to insert: ")

result = insert_middle(original_string, insert_string)
print("Result:", result)
