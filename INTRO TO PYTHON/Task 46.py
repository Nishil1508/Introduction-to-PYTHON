#Write a Python function to check whether a number is in a given range

def is_in_range(num, start, end):

    if start <= num <= end:
        return True
    else:
        return False

number = 5 
start_range = 1
end_range = 10

if is_in_range(number, start_range, end_range):
    print(f"{number} is in the range from {start_range} to {end_range}.")
else:
    print(f"{number} is not in the range from {start_range} to {end_range}.")
