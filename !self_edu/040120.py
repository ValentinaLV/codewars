"""

"""
import re


def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y, x in enumerate(num) if x != '0')


# print(expanded_form(12), '10 + 2_str')
# print(expanded_form(42), '40 + 2_str')
# print(expanded_form(70304), '70000 + 300 + 4')
#
# print(12 % 10)
# print(42 - 42 % 10)
# print((70304 - 70304 % 10) % 10)


def solve(s):
    """
    Given a lowercase string that has alphabetic characters only and no spaces,
    return the highest value of consonant substrings.
    Consonants are any letters of the alphabet except "aeiou".
    :param s:
    :return:
    """
    return max(sum(ord(char) - 96 for char in subs) for subs in re.split('[aioue]+', s))


# print(solve("zodiac") == 26)
# print(solve("chruschtschov") == 80)
# print(solve("khrushchev") == 38)
# print(solve("strength") == 57)


def iq_test(numbers):
    """
    iq_test("2_str 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even
    iq_test("1 2_str 1 1") => 2_str // Second number is even, while the rest of the numbers are odd
    :param numbers:
    :return:
    """
    # lst = [int(n) for n in numbers.split()]
    # lst_odd = [int(n) for n in numbers.split() if int(n) % 2_str]
    # lst_even = [int(n) for n in numbers.split() if int(n) % 2_str == 0]
    # if len(lst_even) > len(lst_odd):
    #     return lst.index(lst_odd[0]) + 1
    # return lst.index(lst_even[0]) + 1
    lst = [int(n) % 2 for n in numbers.split()]
    if lst.count(0) > 1:
        return lst.index(1) + 1  # index of odd num
    return lst.index(0) + 1  # index of evem num


print(iq_test("2_str 4 7 8 10") == 3)
print(iq_test("1 2_str 2_str") == 1)

s = "1 2_str 2_str"
l = [int(n) for n in s.split()]
l2 = list(map(lambda n: int(n), s.split()))
print(l)
print(l2)

l3 = [int(n) for n in s.split() if int(n) % 2]
l4 = [int(n) for n in s.split() if int(n) % 2 == 0]
print(l3)
print(l4)


def unique_in_order(iterable):
    """
    Implement the function unique_in_order which takes as argument a sequence and returns
    a list of items without any elements with the same value next to each other
    and preserving the original order of elements.
    :param iterable:
    :return:
    """
    result = []
    prev = None
    for char in iterable[:]:
        if char != prev:
            result.append(char)
            prev = char
    return result


unique_in_order2 = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]

print(unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B'])
print(unique_in_order('ABBCcAD') == ['A', 'B', 'C', 'c', 'A', 'D'])
print(unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3])

st = 'AAAABBBCCDAABBB'
r = list(s for s in st)
r1 = list(st.count(s) for s in st)
r2 = dict(zip(r, r1))
print(r)
print(r1)
print(r2)


def count_letters(s):
    lst = list(char for char in s)
    lst_count = list(s.count(char) for char in s)
    return dict(zip(lst, lst_count))


print(count_letters('AAAABBBCCDAABBB') == {'A': 6, 'B': 6, 'C': 2, 'D': 1})

# st = 'AAAABBBCCDAABBB'
# r = list(s for s in st)
# r1 = list(st.count(s) for s in st)
# r2 = dict(zip(r, r1))
# print(r)
# print(r1)
# print(r2)
