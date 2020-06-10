from string import ascii_lowercase

revert_ascii_lowercase = list(reversed(ascii_lowercase))
s = list(zip(ascii_lowercase, revert_ascii_lowercase))


def solution(string):
    new = ''
    for a, b in s:
        for c in string:
            if c == a:
                new += b
            else:
                new += c
    return new


# from string import ascii_uppercase
# dict_ascii_upper = list(zip(ascii_uppercase, reversed(ascii_uppercase)))
# LETTERS_UPPER = {letter: char for char, letter in dict_ascii_upper}
# print(LETTERS_UPPER)
# LETTERS = {**LETTERS_LOWER, **LETTERS_UPPER}

from string import ascii_lowercase

dict_ascii_lower = list(zip(ascii_lowercase, reversed(ascii_lowercase)))
LETTERS = {letter: char for char, letter in dict_ascii_lower}


def solution(text):
    reversed_str = ''
    for char in text:
        if char in LETTERS and char.islower():
            reversed_str += LETTERS[char]
        else:
            reversed_str += char
    return reversed_str


print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))


# maximum product of subset
def solution2(lst):
    if len(lst) <= 2 and 0 in lst:
        return max(lst)
    lst = [num for num in lst if num != 0]
    max_product = 1
    for num in lst:
        max_product *= num
    if max_product < 0:
        lst.remove(max([num for num in lst if num < 0]))
        max_product = solution2(lst)
    return max_product


from functools import reduce


def solution3(lst):
    bucket = lst[:]

    state = sum(bucket) % 3
    while state > 0 and bucket:
        if state == 1:
            to_remove = set(bucket) & {1, 4, 7}
            if not to_remove:
                to_remove = set(bucket) & {2, 5, 8}
        elif state == 2:
            to_remove = set(bucket) & {2, 5, 8}
            if not to_remove:
                to_remove = set(bucket) & {1, 4, 7}
        bucket.remove(min(to_remove))
        state = sum(bucket) % 3

    sorted_list = sorted(bucket)[::-1]
    number = ''.join(str(x) for x in sorted_list)
    return int(number) if number else 0


print(solution3([2, -3, 1, 0, -5]))
print(solution3([-2, -3, 4, -5]))
print(solution3([2, 0, 2, 2, 0]))


def solution4(lst):
    pass


print(solution4([3, 1, 4, 1]))
print(solution4([3, 1, 4, 1, 5, 9]))
print(solution4([]))
print(solution4([9, 9, 9, 9]))

import copy

lst = [[1,2], [2,3]]
# lst2 = lst.copy()
# lst2[0][1] = 3
# print(lst)
# print(lst2)
lst2 = copy.deepcopy(lst)
lst2[0][1] = 3
print(lst)
print(lst2)
