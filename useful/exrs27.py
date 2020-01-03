"""
https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

https://www.codewars.com/kata/5aba780a6a176b029800041c

https://www.codewars.com/kata/5d50e3914861a500121e1958
"""
from string import ascii_lowercase


def find_short(string):
    return min(len(s) for s in string.split())


def max_multiple(divisor_num, bound_num):
    return bound_num - (bound_num % divisor_num)


def add_letters(*letters):
    alphabet = ascii_lowercase
    return alphabet[sum([alphabet.index(letter) for letter in letters]) % 26]