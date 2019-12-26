"""
https://www.codewars.com/kata/5aba780a6a176b029800041c

https://www.codewars.com/kata/5727bb0fe81185ae62000ae3
"""


def max_multiple(divisor_num, bound_num):
    return bound_num - (bound_num % divisor_num)


def clean_string(s):
    """
    Assume "#" is like a backspace in string.
    This means that string "a#bc#d" actually is "bd"
    Your task is to process a string with "#" symbols.
    :param s:
    :return:
    """
    ns = []
    for l in s:
        if l != '#':
            ns.append(l)
        elif ns:
            ns.pop()
    return ''.join(ns)


print(clean_string('abc#d##c'))

print(clean_string('abc#d##c') == "ac")
print(clean_string('abc####d##c#') == "")
print(clean_string("#######") == "")
print(clean_string("") == "")
