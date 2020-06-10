def swap_case(string):
    new_string = ''
    for char in string:
        if char.islower():
            new_string += char.upper()
        elif char.isupper():
            new_string += char.lower()
        else:
            new_string += char
    return new_string


def split_and_join(line):
    return '-'.join(line.split())


def mutate_string(string: str, position, character):
    new_str = ''
    for i, c in enumerate(string):
        if i == position:
            new_str += character
        else:
            new_str += c
    return new_str


def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if sub_string == string[i:len(sub_string) + i]:
            count += 1
    return count

import textwrap
def wrap(string, max_width):
    # i = 0
    # s = []
    # while len(string) + i >= max_width:
    #     s.append(string[i:max_width])
    #     i = max_width
    #     max_width += i
    # return s
    return "\n".join(textwrap.wrap(string, max_width))


def solve(s):
    return ' '.join(name.capitalize() for name in s.split(' '))


if __name__ == '__main__':
    print(swap_case('HackerRank.com presents "Pythonist 2".'))
    print(split_and_join("this is a string"))
    print(mutate_string('abracadabra', 5, 'k'))
    print(count_substring('ABCDCDC', 'CDC'))
    # s = input()
    # print(any(c.isalnum() for c in s))
    # print(any(c.isalpha() for c in s))
    # print(any(c.isdigit() for c in s))
    # print(any(c.islower() for c in s))
    # print(any(c.isupper() for c in s))
    print(wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4))
    print(solve('hello   world  lol'))
