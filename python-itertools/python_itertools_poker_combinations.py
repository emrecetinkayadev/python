import itertools

ranks = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
ranks = [str(rank) for rank in ranks]

# print(ranks)

suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
deck = [card for card in itertools.product(ranks, suits)]

# for (index, card) in enumerate(deck):
#     print(1 + index, card

hands = [hard for hard in itertools.combinations(deck, 5)]
print(len(hands))


print(list(map(lambda x : x * x, [1, 2, 3])))