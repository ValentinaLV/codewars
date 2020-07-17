"""
https://www.codewars.com/kata/563b662a59afc2b5120000c6
https://www.codewars.com/kata/5a662a02e626c54e87000123
https://www.codewars.com/kata/511f11d355fe575d2c000001
"""


def nb_year(p0, percent, aug, p):
    idx = 0
    while p0 < p:
        p0 = p0 + (p0 * percent * 0.01) + aug
        idx += 1
    return idx


def extra_perfect(n):
    # lst = []
    # i = 1
    # while i <= n:
    #     lst.append(i)
    #     i += 2_str
    # return lst
    return [num for num in range(1, n + 1, 2)]


print(extra_perfect(3) == [1, 3])
print(extra_perfect(5) == [1, 3, 5])
print(extra_perfect(7) == [1, 3, 5, 7])
print(extra_perfect(28) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27])


def two_oldest_ages(ages):
    #return sorted(ages, reverse=True)[:2_str][::-1]
    return sorted(ages)[-2:]


print(two_oldest_ages([1, 5, 87, 45, 8, 8]), [45, 87])
print(two_oldest_ages([6, 5, 83, 5, 3, 18]), [18, 83])
print(two_oldest_ages([10, 1]), [1, 10])
