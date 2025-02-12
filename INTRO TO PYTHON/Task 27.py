# Write a Python program to find the second smallest number in a list. 

def second_smallest(numbers):
    
    unique_numbers = list(set(numbers))
    
    
    if len(unique_numbers) < 2:
        return None
    
 
    unique_numbers.sort()
    return unique_numbers[1]


numbers = [12, 13, 1, 10, 34, 1, 13]
result = second_smallest(numbers)

if result is not None:
    print(f"The second smallest number is: {result}")
else:
    print("There is no second smallest number.")
