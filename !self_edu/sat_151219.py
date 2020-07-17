def array_diff(a: list, b: list):
    return [num for num in a if num not in b]
    # for i in a:
    #     if i in b:
    #         a.remove(i)
    # return a


print(array_diff([1, 2], [1]) == [2])


def disem_vowel(string):
    """
    Your task is to write a function that takes a
    string and return a new string with all vowels removed.
    :param string:
    :return:
    """
    return ''.join([s for s in string if s not in "aeiouAEIOU"])


print(disem_vowel("This website is for losers LOL!"))
print(disem_vowel("This website is for losers LOL!") == "Ths wbst s fr lsrs LL!")


def binary_array_to_number(arr):
    """
    Given an array of ones and zeroes, convert
    the equivalent binary value to an integer.
    Eg: [0, 0, 0, 1] is treated as 0001
    which is the binary representation of 1.
    :param arr:
    :return:
    """
    return int(''.join(map(str, arr)), 2)


print(binary_array_to_number([0, 0, 0, 1]) == 1)


def get_count(input_str: str):
    """
    Return the number (count) of vowels in the given string.
    We will consider a, e, i, o, and u as vowels for this Kata.
    The input string will only consist of lower case letters and/or spaces.
    :param input_str:
    :return:
    """
    # num_vowels = 0
    # vowels = 'aeiou'
    # for s in input_str:
    #     if s in vowels:
    #         num_vowels += 1
    # return num_vowels
    return sum(s in 'aeiou' for s in input_str)


print(get_count("abracadabra") == 5)

import string
def DNA_strand(dna: str):
    """
    In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
    You have function with one side of the DNA (string, except for Haskell);
    you need to get the other complementary side. DNA strand is never empty or
    there is no DNA at all (again, except for Haskell).
    :param dna:
    :return:
    """
    pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(pairs[d] for d in dna)
    #return dna.translate(string.maketrans("ATCG", "TAGC"))


print(DNA_strand("ATTGC"))


def xo(s: str):
    """
    Check to see if a string has the same amount of 'x's and 'o's.
    The method must return a boolean and be case insensitive. The string can contain any char.
    :param s:
    :return:
    """
    return s.lower().count('x') == s.lower().count('o')


print(xo("ooxXm"))


def basic_op(operator, value1, value2):
    """
    Basic Mathematical Operations
    :param operator:
    :param value1:
    :param value2:
    :return:
    """
    return {'+': value1 + value2,
            '-': value1 - value2,
            '*': value1 * value2,
            '/': value1 / value2}.get(operator)


def square_digits(num):
    """
    Square Every Digit
    :param num:
    :return:
    """
    return int(''.join([str(int(s)**2) for s in str(num)]))


print(square_digits(9119) == 811181)


def high_and_low(numbers: str):
    """
    In this little assignment you are given a string of
    space separated numbers, and have to return the highest and lowest number.
    :param numbers:
    :return:
    """
    # arr = numbers.split(' ')
    # return str(max(map(int, arr))) + ' ' + str(min(map(int, arr)))
    arr = list(map(int, numbers.split(' ')))
    return "{} {}".format(max(arr), min(arr))


print(high_and_low("1 2_str 3 4 5") == "5 1")


def series_sum(num):
    """
    Sum of the first nth term of Series
    1 + 1/4 + 1/7 + 1/10 + 1/13 + ...
    :param n:
    :return:
    """
    return '{:.2f}'.format(sum(1.00/(3 * i + 1) for i in range(num)))


print(series_sum(2) == '1.25')


def sum_two_smallest_numbers(numbers: list):
    """
    Sum of two lowest positive integers.
    :param numbers:
    :return:
    """
    return sum(sorted(numbers)[:2])


print(sum_two_smallest_numbers([5, 8, 12, 18, 22]) == 13)


