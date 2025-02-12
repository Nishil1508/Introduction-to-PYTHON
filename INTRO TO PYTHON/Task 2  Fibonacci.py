# Write a Python program to get the Fibonacci series of given range
def fibonacci(n):
    fib_series = [0, 1]  # Starting values
    for i in range(2, n):
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)
    return fib_series[:n]  # Return only up to the required range

# Get user input
num = int(input("Enter the range for Fibonacci series: "))
print("Fibonacci Series:", fibonacci(num))
