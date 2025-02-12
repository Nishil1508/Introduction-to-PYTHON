#Write a Python program to append text to a file and display the text.

def append_and_display(file_name, text_to_append):
    try:
        
        with open(file_name, 'a') as file:
            file.write(text_to_append + "\n")  
        
       
        with open(file_name, 'r') as file:
            content = file.read()  
            print("Updated file content:")
            print(content) 
    except Exception as e:
        print(f"An error occurred: {e}")


file_name = 'example.txt'  
text_to_append = "This is the new text being appended."

append_and_display(file_name, text_to_append)
