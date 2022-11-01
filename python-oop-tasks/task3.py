'''
Task 3

Implement a function `get_shortest_word(s: str) -> str` which
returns the longest word in the given string.
The word can contain any symbols except whitespaces (` `, `\n`, `\t` and so on).
If there are multiple longest words in the string with a same length
return the word that occurs first.

'''

def get_shortest_word(s: str) -> str:
    max_word = ""
    words = s.split()
    for word in words:
        if len(word) > len(max_word):
            max_word = word
    return max_word

print(get_shortest_word('Python is simple and effective!'))

print(get_shortest_word('Any pythonista like namespaces a lot.'))
