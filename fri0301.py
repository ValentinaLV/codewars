"""

"""
from string import ascii_lowercase

def high(lst):
    """
    Highest Scoring Word
    :param x:
    :return:
    """
    # r = []
    # for item in lst.split():
    #     scores = [sum(ord(char) - 96 for char in item)]
    #     r.append(scores)
    # return lst.split()[r.index(max(r))]
    return max(lst.split(), key=lambda k: sum(ord(char) - 96 for char in k))


print(high('man i need a taxi up to ubud') == 'taxi')
print(high('what time are we climbing up the volcano') == 'volcano')
print(high('take me to semynak') == 'semynak')

l = 'man i need a taxi up to ubud'.split()
print(l)
# d = {}
# for i, l in enumerate(ascii_lowercase):
#     d[l] = i + 1
# print(d)
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11,
     'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,
     'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

r = [len(el) for i, el in enumerate(l)]
r1 = [ord(char) - 96 for i, el in enumerate(l) for char in el]
r2 = [ascii_lowercase.index(char) + 1 for i, el in enumerate(l) for char in el]
print(r1)
print(r2)