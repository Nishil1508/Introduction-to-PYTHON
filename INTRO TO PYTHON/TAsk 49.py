# Write a Python program to read an entire text file.

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()  
            print(content) 
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = 'example.txt'  
read_file(file_name)
