# Create a list of squares of numbers between 1 and 30
squares = [i**2 for i in range(1, 31)]

first_5 = squares[:5]

last_5 = squares[-5:]

print("First 5 elements:", first_5)
print("Last 5 elements:", last_5)
