"""

"""
from datetime import date


def count_digits(text: str) -> int:
    return len(list(n for n in text if n.isdigit()))


def days_diff(a, b):
    # your code here
    return abs((date(*a) - date(*b)).days)


def is_all_upper(text: str) -> bool:
    # bool("   ".strip()) == False
    return text.isupper() or bool(text.strip()) is False or text.isdigit()
    # return all([c.isupper() for c in text if c.isalpha()])


from typing import Iterable


def replace_first(items: list) -> Iterable:
    # your code here
    if len(items) > 1:
        items.append(items.pop(0))
        # items = items[1:]+[items[0]]
    return items


if __name__ == '__main__':
    # print("Example:")
    # print(count_digits('hi'))
    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert count_digits('hi') == 0
    # assert count_digits('who is 1st here') == 1
    # assert count_digits('my numbers is 2') == 1
    # assert count_digits('This picture is an oil on canvas '
    #                     'painting by Danish artist Anna '
    #                     'Petersen between 1845 and 1910 year') == 8
    # assert count_digits('5 plus 6 is') == 2
    # assert count_digits('') == 0
    # print("Coding complete? Click 'Check' to earn cool rewards!")
    # print("Example:")
    # print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    # assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    # assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    # print("Coding complete? Click 'Check' to earn cool rewards!")

    # print("Example:")
    # print(is_all_upper("     "))
    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert is_all_upper('ALL UPPER') == True
    # assert is_all_upper('all lower') == False
    # assert is_all_upper('mixed UPPER and lower') == False
    # assert is_all_upper('') == True
    # print("Coding complete? Click 'Check' to earn cool rewards!")

    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
