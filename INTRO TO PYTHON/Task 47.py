# Write a Python function to check whether a number is perfect or not.

def is_perfect_number(num):
    if num <= 0:
        return False 
    
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0: 
            divisor_sum += i
    
    if divisor_sum == num:
        return True
    else:
        return False

number = 28
if is_perfect_number(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
