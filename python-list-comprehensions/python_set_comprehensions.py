# Set comprehensions.
old = [2, 3, 4, 5, 6, 7, 2, 1]

# new set with mod and squared.
new_set = {i*i for i in old if i%2 == 0}
print(new_set)
