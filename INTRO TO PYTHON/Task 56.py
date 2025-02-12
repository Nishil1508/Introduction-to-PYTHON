# Write a Python program to count the number of lines in a text file.

def count_lines_in_file(file_name):
    try:
        
        with open(file_name, 'r') as file:
           
            line_count = sum(1 for line in file)
        return line_count
    
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0


file_name = 'example.txt' 
line_count = count_lines_in_file(file_name)

if line_count > 0:
    print(f"The file '{file_name}' contains {line_count} lines.")
else:
    print("No content or error in counting the lines.")
