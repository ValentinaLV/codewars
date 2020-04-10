"""

"""


def sortme(words):
    return sorted(words, key=lambda x: x.lower())


print(sortme(["Hello", "there", "I'm", "fine"]), ["fine", "Hello", "I'm", "there"])
print(sortme(["C", "d", "a", "B"]), ["a", "B", "C", "d"])
print(sortme(["CodeWars"]), ["CodeWars"])


def letter_count(string):
    return {c: string.count(c) for c in string}


print(letter_count("codewars") == {"a": 1, "c": 1, "d": 1, "e": 1, "o": 1, "r": 1, "s": 1, "w": 1})
print(letter_count("activity"), {"a": 1, "c": 1, "i": 2, "t": 2, "v": 1, "y": 1})
print(letter_count("arithmetics"), {"a": 1, "c": 1, "e": 1, "h": 1, "i": 2, "m": 1, "r": 1, "s": 1, "t": 2})
print(letter_count("traveller"), {"a": 1, "e": 2, "l": 2, "r": 2, "t": 1, "v": 1})
print(letter_count("daydreamer"), {"a": 2, "d": 2, "e": 2, "m": 1, "r": 2, "y": 1})


def multiplication_table(row, col):
    return [[(i + 1) * (j + 1) for i in range(col)] for j in range(row)]


print(multiplication_table(2, 2), [[1, 2], [2, 4]])
print(multiplication_table(3, 3), [[1, 2, 3], [2, 4, 6], [3, 6, 9]])
