nums = [1, 2, 3]

for num in nums:
    print(num)

# Lets check iter method.
i_nums = iter(nums)  # or nums.__iter__()
print(i_nums)
print(dir(i_nums))

# Each time next method remembers where is stayed.
print(next(i_nums))
print(next(i_nums))
print(next(i_nums))

while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break

#  ----------------------------------------------------------------

class MyRange:
    def __init__(self, start, end) -> None:
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


nums = MyRange(1, 10)

print(nums.__iter__)
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))

#  ----------------------------------------------------------------

def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1


nums = my_range(1, 10)
