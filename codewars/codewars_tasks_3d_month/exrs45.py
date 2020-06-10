"""
https://www.codewars.com/kata/5d5a7525207a674b71aa25b5

https://www.codewars.com/kata/5264d2b162488dc400000001
"""


def odd_row(num):
    return list(range(num ** 2 - num + 1, num ** 2 + num, 2))


def spin_words2(string):
    return string[::-1]
    # lst = [c for c in sentence]
    # lst.reverse()
    # return ''.join(lst)
    #return ''.join(reversed(sentence))


def spin_words(string):
    w = [word for word in string.split(" ")]
    w = [word if len(word) < 5 else word[::-1] for word in w]
    return " ".join(w)


print(spin_words("Welcome") == "emocleW")
print(spin_words('sroirraw wollef yeH'), 'Hey wollef sroirraw')
