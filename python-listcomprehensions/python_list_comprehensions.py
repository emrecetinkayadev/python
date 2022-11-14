# List Comprehensions
old = [2, 3, 4, 5, 6, 7]

# Only find even numbers.
new = [i for i in old if i % 2 == 0]
print(new)

# Calculating square's
square = [i*i for i in old]
print(square)
