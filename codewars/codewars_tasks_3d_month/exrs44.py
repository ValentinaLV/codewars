"""
https://www.codewars.com/kata/56d904db9963e9cf5000037d

https://www.codewars.com/kata/523f5d21c841566fde000009
"""


def it(var1, var2):
    return var1 | var2


def array_diff(lst1, lst2):
    return [item for item in lst1 if item not in lst2]


print(array_diff([1, 2], [1]) == [2])
print(array_diff([1, 2, 2], [1]) == [2, 2])
print(array_diff([1, 2, 2], [2]) == [1])
print(array_diff([1, 2, 2], []) == [1, 2, 2])
print(array_diff([], [1, 2]) == [])
