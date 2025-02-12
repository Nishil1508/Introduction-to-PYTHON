#Write a Python program to read a file line by line and store it into a list 

def read_file_to_list(file_name):
    try:
       
        with open(file_name, 'r') as file:
            lines = file.readlines() 
           
            lines = [line.strip() for line in lines]
            return lines 
    
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


file_name = 'example.txt'  
lines = read_file_to_list(file_name)

if lines:
    print("File content as list:")
    print(lines)
else:
    print("No content to display.")
