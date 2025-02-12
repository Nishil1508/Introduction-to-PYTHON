# Write a Python program to read last n lines of a file. 

def read_last_n_lines(file_name, n):
    try:
    
        with open(file_name, 'r') as file:
            
            lines = file.readlines()

            if len(lines) < n:
                print("The file has fewer than", n, "lines. Displaying all lines:")
                print("".join(lines))
            else:
                
                last_n_lines = lines[-n:]
                print("Last", n, "lines of the file:")
                print("".join(last_n_lines))
    
    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
 
