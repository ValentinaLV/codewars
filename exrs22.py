"""
https://www.codewars.com/kata/580a4734d6df748060000045

https://www.codewars.com/kata/58a08e622e7fb654a300000e
"""


def is_sorted_and_how(arr):
    """
    "yes, ascending" - if the numbers in the array are sorted in an ascending order
    "yes, descending" - if the numbers in the array are sorted in a descending order
    "no" - otherwise
    :param arr:
    :return:
    """
    if sorted(arr) == arr:
        return "yes, ascending"
    elif sorted(arr, reverse=True) == arr:
        return "yes, descending"
    else:
        return "no"


def sort_grades(lst):
    grades_info = ['VB', 'V0', 'V0+', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6',
                   'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17']
    return sorted(lst, key=lambda g: grades_info.index(g))


