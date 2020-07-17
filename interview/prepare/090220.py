def num_args(*args):
    """

    :return:
    """
    return len(args)


def remove_dups(lst):
    """
    Create a function that takes a list of items, removes all duplicate items and returns a
    new list in the same sequential order as the old list (minus duplicates).
    :return:
    """
    # result_lst = []
    # for item in lst:
    #     if item not in result_lst:
    #         result_lst.append(item)
    # return result_lst
    # return sorted(set(lst), key=lst.index)
    return [item for i, item in enumerate(lst) if item not in lst[:i]]


print(remove_dups(['John', 'Taylor', 'John']))


def sum_two_smallest_nums(lst):
    """
    Create a function that takes a list of numbers and returns the sum
    of the two lowest positive numbers.
    :param lst:
    :return:
    """
    return sum(sorted([num for num in lst if num > 0])[:2])


print(sum_two_smallest_nums([879, 953, 694, -847, 342, 221, -91, -723, 791, -587]))  # 563


def median(lst):
    lst = sorted(lst)
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2
    return lst[(len(lst) - 1) // 2]


print(median([21.4323, 432.54, 432.3, 542.4567]))  # 432.42
print(median([2, 5, 6, 2, 6, 3, 4]))  # 4


from functools import reduce
def index_multiplier(lst):
    """
    Return the sum of all items in a list, where each item is
    multiplied by its index (zero-based). For empty lists, return 0.
    :return:
    """
    return sum([i * item for i, item in enumerate(lst)]) if lst else 0


print('index_multiplier')
print(index_multiplier([1, 2, 3, 4, 5]))  # 40


def puzzle_pieces(lst1, lst2):
    """
    Write a function that takes two lists and adds the first element in the first list with the
    first element in the second list, the second element in the first list with the
    second element in the second list, etc, etc. Return True if all element combinations
    add up to the same number. Otherwise, return False.
    :param lst1:
    :param lst2:
    :return:
    """
    if len(lst1) == len(lst2):
        return len(set([s1 + s2 for s1, s2 in zip(lst1, lst2)])) == 1
    return False


print(puzzle_pieces([1, 8, 5, 0, -1, 7], [0, -7, -4, 1, 2, -6]))


def minutes_to_seconds(minutes):
    """
    You are given the length of a video in minutes. The format is mm:ss
    (e.g.: "02:54"). Create a function that takes the video length and return it in seconds.
    :param minutes:
    :return:
    """
    lst = [int(n) for n in minutes.split(':')]
    return 60 * lst[0] + lst[1]


print(minutes_to_seconds("13:56"))  # 836

from functools import reduce


def total_volume(*args):
    total = 0
    for lst in args:
        total += reduce(lambda x, y: x * y, lst)
    return total


print(total_volume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1]))  # 63


def is_int_array(lst):
    """

    :param arr:
    :return:
    """
    return isinstance(lst, list) and all(isinstance(item, (int, float)) and item == int(item) for item in lst)


print(is_int_array([1, 2, 3, 4]))
print(is_int_array([1, 2, 3, 'Hello']))
print(is_int_array([]))


def productFib(prod):
    num1, num2 = 0, 1
    while prod > num1 * num2:
        num1, num2 = num2, num1 + num2
    return [num1, num2, prod == num1 * num2]




