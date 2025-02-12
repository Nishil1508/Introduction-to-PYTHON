#  Sample string:'w3resource' Expected output: {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}


input_string = 'w3resource'

char_count = {}

for char in input_string:
    if char in char_count:
       
        char_count[char] += 1
    else:
       
        char_count[char] = 1

print("Character count dictionary:", char_count)
