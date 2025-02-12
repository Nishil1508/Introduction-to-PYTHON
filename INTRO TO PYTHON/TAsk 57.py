#Write a Python program to count the frequency of words in a file.

def count_word_frequency(file_name):
    try:
        
        word_count = {}

     
        with open(file_name, 'r') as file:
            
            for line in file:
                
                words = line.split()
                for word in words:
                    
                    word = word.lower()
                 
                    word = word.strip('.,!?()[]{}":;')
                    
                    
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
        
        return word_count

    except FileNotFoundError:
        print(f"The file '{file_name}' does not exist.")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}


file_name = 'example.txt'  
word_count = count_word_frequency(file_name)

if word_count:
    print(f"Word frequency in the file '{file_name}':")
    for word, count in word_count.items():
        print(f"{word}: {count}")
else:
    print("No content to display.")
