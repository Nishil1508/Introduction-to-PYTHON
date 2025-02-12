# Write a Python program to read first n lines of a file.

def read_first_n_lines(file_name, n):
    try:
       
        with open(file_name, 'r') as file:
           
            for i in range(n):
                line = file.readline() 
                if line:  
                    print(line, end='') 
                else:
                    print("\nReached the end of the file.")
                    break
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_name = 'example.txt' 
n = 3  

read_first_n_lines(file_name, n)
