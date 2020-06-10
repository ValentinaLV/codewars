"""
https://www.codewars.com/kata/5583090cbe83f4fd8c000051

https://www.codewars.com/kata/574b3b1599d8f897470018f6

https://www.codewars.com/kata/570a6a46455d08ff8d001002
"""


def digitize(num):
    return list(reversed([int(n) for n in str(num)]))


print(digitize(35231) == [1, 3, 2, 5, 3])


def get_real_floor(num):
    """

    :param num:
    :return:
    """
    if num <= 0:
        return num
    if num < 13:
        return num - 1
    if num > 13:
        return num - 2


print(get_real_floor(1), 0)
print(get_real_floor(5), 4)
print(get_real_floor(15), 13)


def no_boring_zeros(num):
    if num != 0:
        return int(str(num).rstrip('0'))
    return 0


print(no_boring_zeros(1450) == 145)
print(no_boring_zeros(960000) == 96)
print(no_boring_zeros(1050) == 105)
print(no_boring_zeros(-1050) == -105)
print(no_boring_zeros(0) == 0)
