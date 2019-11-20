"""
exercises from 18112019
"""


def get_count(inputStr):
    """
    Return the number (count) of vowels in the given string.
    We will consider a, e, i, o, and u as vowels for this Kata.
    The input string will only consist of lower case letters and/or spaces.
    :param input_str:
    :return:
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    return sum(inputStr.count(vowel) for vowel in vowels)


def vert_mirror(strng):
    """

    :param strng:
    :return:
    """
    return '\n'.join(s[::-1] for s in strng.split('\n'))


def hor_mirror(strng):
    """

    :param strng:
    :return:
    """
    return '\n'.join(reversed(strng.split('\n')))


def oper(fct, s):
    """

    :param fct:
    :param s:
    :return:
    """
    return fct(s)
