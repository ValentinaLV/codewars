from typing import Iterable


def remove_el_from_lst(lst: list, remove_list: list) -> list:
    """
    The original list is : [1, 3, 4, 6, 7]
    The original list is : [3, 6]
    The list after performing remove operation is : [1, 4, 7]
    :return:
    """
    return [i for i in lst if i not in remove_list]


def remove_all_before(items: list, border: int) -> Iterable:
    # your code here
    return items[items.index(border):] if border in items else items


def end_zeros(num: int) -> int:
    # your code here
    i = -1
    count_zeros = 0
    if num == 0:
        return 1
    while str(num)[i] == '0':
        count_zeros += 1
        i -= 1
    return count_zeros


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 1, 2, 2, 3, 3], 2)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
