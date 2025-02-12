# Write a Python program to copy the contents of a file to another file.

def copy_file_contents(source_file, destination_file):
    try:
     
        with open(source_file, 'r') as source:
            
            content = source.read()
        
        
        with open(destination_file, 'w') as destination:
           
            destination.write(content)
        
        print(f"Contents of '{source_file}' have been copied to '{destination_file}'.")

    except FileNotFoundError:
        print(f"The file '{source_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


source_file = 'source.txt'  
destination_file = 'destination.txt'  

copy_file_contents(source_file, destination_file)
