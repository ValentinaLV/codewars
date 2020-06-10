"""
https://www.codewars.com/kata/5ad90fb688a0b74111000055

https://www.codewars.com/kata/550498447451fbbd7600041c
"""


def comp(lst1, lst2):
    if lst1 and lst2:
        return sorted(x ** 2 for x in lst1) == sorted(lst2)
    return lst1 == lst2 == []
