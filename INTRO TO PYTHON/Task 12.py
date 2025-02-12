# Write a Python program to count the occurrences of each word in a given Sentence

def word_count(sentence):
    # Convert the sentence to lowercase and split into words
    words = sentence.lower().split()
    frequency = {}
    
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
            
    return frequency

# Get user input
sentence = input("Enter a sentence: ")

# Calculate and print the word frequencies
result = word_count(sentence)
print("Word frequencies:", result)
