"""
https://www.codewars.com/kata/5a03b3f6a1c9040084001765
https://www.codewars.com/kata/5af15a37de4c7f223e00012d
https://www.codewars.com/kata/5ac6932b2f317b96980000ca
"""


def angle(number):
    return 180 * (number - 2)


def men_from_boys(lst):
    evens = []
    odds = []
    for num in sorted(set(lst)):
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    return evens + sorted(odds, reverse=True)


print(men_from_boys([7, 3, 14, 17]) == [14, 17, 7, 3])
print(men_from_boys([2, 43, 95, 90, 37]) == [2, 90, 95, 43, 37])
print(men_from_boys([20, 33, 50, 34, 43, 46]) == [20, 34, 46, 50, 43, 33])


def min_value(lst_of_nums):
    return int("".join(str(num) for num in sorted(set(lst_of_nums))))


print(min_value([1, 3, 1]) == 13)
print(min_value([4, 7, 5, 7]) == 457)
print(min_value([4, 8, 1, 4]) == 148)
