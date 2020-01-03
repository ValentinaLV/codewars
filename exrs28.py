"""
https://www.codewars.com/kata/5d50e3914861a500121e1958

https://www.codewars.com/kata/5e0607115654a900140b3ce3
"""
from string import ascii_lowercase


def add_letters(*letters):
    alphabet = ascii_lowercase
    return alphabet[sum([alphabet.index(letter) + 1 for letter in letters]) % 26 - 1]


def sequence(num):
    return int(bin(num)[2:], 3)
