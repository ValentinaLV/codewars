"""
https://www.codewars.com/kata/5e4e8f5a72d9550032953717
https://www.codewars.com/kata/5866a58b9cbc02c4f8000cac
"""


def f():
    yield 1, 1
    for a, b in f():
        yield a, a + b
        yield a + b, b


all_rationals = f


def make_move(sticks):
    return sticks % 4
