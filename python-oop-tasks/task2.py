'''
Task 2

Implement a function `get_pairs(lst: List) -> List[Tuple]`
which returns a list of tuples containing pairs of elements.
Pairs should be formed as in the example.
If there is only one element in the list return `None` instead.

'''

def get_pairs(L):
    k = 2
    bubbleList = []
    for i in range(len(L)-1):
        bubbleList.append(tuple(L[i:k]))
        k += 1
    return bubbleList

print(get_pairs([1, 2, 3, 8, 9]))
print(get_pairs(['need', 'to', 'sleep', 'more']))