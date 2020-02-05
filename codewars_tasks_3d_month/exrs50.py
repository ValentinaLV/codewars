"""
https://www.codewars.com/kata/5c46ea433dd41b19af1ca3b3

https://www.codewars.com/kata/5d7d05d070a6f60015c436d1
"""
from re import findall


def hex_word_sum(string):
    string = string.translate(str.maketrans('OS', '05'))
    return sum(int(x, 16) for x in findall(r'\b[\dA-F]+\b', string))


print(hex_word_sum('DEFACE') == 14613198)
print(hex_word_sum('SAFE') == 23294)
print(hex_word_sum('CODE') == 49374)
