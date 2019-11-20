"""
exercises from 19112019
"""
import math


def century(year):
    """
    Given a year, return the century it is in.
    :param year: int
    :return: int
    """
    return math.ceil(year / 100)


def century_sec(year):
    """
    Given a year, return the century it is in.
    :param year: int
    :return: int
    """
    return (year - 1) // 100 + 1


def multiple_of_index(arr):
    """
    Return a new array consisting of elements which are multiple of their own index in input array (length > 1).
    :param arr: list
    :return: list
    """
    return [arr[i] for i in range(1, len(arr)) if arr[i] % i == 0]


#print(multiple_of_index([22, -6, 32, 82, 9, 25]))


def expanded_form(num):
    """
    You will be given a number and you will need to return it as a string in Expanded Form. For example:
    expanded_form(42) # Should return '40 + 2'
    expanded_form(70304) # Should return '70000 + 300 + 4'
    :param num: int
    :return: str
    """
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y, x in enumerate(num) if x != '0')