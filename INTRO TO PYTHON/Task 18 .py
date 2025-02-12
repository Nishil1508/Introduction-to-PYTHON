#Write a Python function to get the largest number, smallest num and sum of all from a list. 
def list_stats(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    total_sum = sum(numbers)
    
    return largest, smallest, total_sum

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

largest, smallest, total_sum = list_stats(numbers)

print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print(f"Sum of all numbers: {total_sum}")
