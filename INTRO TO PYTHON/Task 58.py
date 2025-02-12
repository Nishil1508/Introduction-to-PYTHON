#Write a Python program to write a list to a file. 

def write_list_to_file(file_name, my_list):
    try:
       
        with open(file_name, 'w') as file:
            
            for item in my_list:
                file.write(f"{item}\n")
        print(f"List successfully written to '{file_name}'")
    except Exception as e:
        print(f"An error occurred: {e}")


my_list = ['apple', 'banana', 'cherry', 'date']
file_name = 'output.txt'

write_list_to_file(file_name, my_list)
