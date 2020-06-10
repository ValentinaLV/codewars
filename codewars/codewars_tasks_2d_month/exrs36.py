"""
https://www.codewars.com/kata/5da9af1142d7910001815d32

https://www.codewars.com/kata/56135a61f8b29814340000cd
"""
from math import floor


def get_score(lst) -> int:
    level = 1
    score = []
    count = 0
    points = {0: 0, 1: 40, 2: 100, 3: 300, 4: 1200}
    for i in lst:
        score.append(points[i] * level)
        count += i
        level = floor(count / 10) + 1
    return sum(score)
