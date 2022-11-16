import itertools

# Count is like a range generator
# for i in itertools.count(0, 5):
#     print(i)

counter = itertools.count(0, 5)

print(type(counter))
print(dir(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

