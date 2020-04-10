"""
https://www.codewars.com/kata/59590976838112bfea0000fa/train/python
https://www.codewars.com/kata/5208f99aee097e6552000148/train/python
"""


def beggars(values, n):
    return [sum(values[i::n]) for i in range(n)]


print(beggars([1, 2, 3, 4, 5], 1), [15])
print(beggars([1, 2, 3, 4, 5], 2), [9, 6])
print(beggars([1, 2, 3, 4, 5], 3), [5, 7, 3])
print(beggars([1, 2, 3, 4, 5], 6), [1, 2, 3, 4, 5, 0])
print(beggars([1, 2, 3, 4, 5], 0), [])


def solution(string):
    return ''.join(' ' + char if char.isupper() else char for char in string)


print(solution("helloWorld"), "hello World")
print(solution("camelCase"), "camel Case")
print(solution("breakCamelCase"), "break Camel Case")


def count(string):
    return {c: string.count(c) for c in string}


print(count('aba'), {'a': 2, 'b': 1})
print(count(''), {})

print({'a': 2, 'b': 1})
