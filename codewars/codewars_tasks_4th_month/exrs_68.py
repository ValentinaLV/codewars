"""
https://www.codewars.com/kata/5dae2599a8f7d90025d2f15f
https://www.codewars.com/kata/569b5cec755dd3534d00000f
"""
from math import log2


def consecutive_ducks(num):
    return not log2(num).is_integer()


from math import ceil


def new_avg(arr, new_avg):
    result = ceil(new_avg * (len(arr) + 1) - sum(arr))
    if result <= 0:
        raise ValueError('error')
    else:
        return result
