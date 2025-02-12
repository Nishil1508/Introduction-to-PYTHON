#Write a Python program to read a file line by line store it into a variable.

def read_file_to_variable(file_name):
    try:
        content = ""  
        with open(file_name, 'r') as file:
            for line in file:
                content += line  
        return content
    
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

file_name = 'example.txt'  
content = read_file_to_variable(file_name)

if content:
    print("File content stored in variable:")
    print(content)
else:
    print("No content to display.")
