"""
https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9


"""


def find_short(string):
    return min(len(s) for s in string.split())


def max_multiple(divisor_num, bound_num):
    return bound_num - (bound_num % divisor_num)

