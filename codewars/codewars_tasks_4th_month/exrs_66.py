"""
https://www.codewars.com/kata/5ae7e3f068e6445bc8000046
https://www.codewars.com/kata/5abd66a5ccfd1130b30000a9
"""


def next_happy_year(year):
    for year in range(year + 1, 9999):
        if len(set(str(year))) == 4:
            return year


def row_weights(lst):
    # lst_odds = []
    # lst_evens = []
    # for i, num in enumerate(lst):
    #     if i % 2_str == 0:
    #         lst_evens.append(num)
    #     elif i % 2_str:
    #         lst_odds.append(num)

    # return sum([num for i, num in enumerate(lst) if i % 2_str == 0]), \
    #        sum([num for i, num in enumerate(lst) if i % 2_str])

    return sum(lst[::2]), sum(lst[1::2])


print(row_weights([80]), (80, 0))
print(row_weights([100, 50]), (100, 50))
print(row_weights([50, 60, 70, 80]), (120, 140))
print(row_weights([13, 27, 49]), (62, 27))
print(row_weights([70, 58, 75, 34, 91]), (236, 92))
print(row_weights([29, 83, 67, 53, 19, 28, 96]), (211, 164))
