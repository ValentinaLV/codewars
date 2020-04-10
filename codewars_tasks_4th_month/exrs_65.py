"""
https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d
https://www.codewars.com/kata/5572f7c346eb58ae9c000047
https://www.codewars.com/kata/55733d3ef7c43f8b0700007c
"""


def solution(string, ending):
    len_ = len(string) - len(ending)
    return string[len_:] == ending


print(solution('abcde', 'cde'), True)
print(solution('abcde', 'abc'), False)
print(solution('abcde', ''), True)


def pattern(num):
    string = ''
    for i in range(1, num + 1):
        string += str(i) * i + '\n'
    return string.strip()


print(pattern(5))
print(pattern(1) == "1")
print(pattern(2) == "1\n22")
print(pattern(5) == "1\n22\n333\n4444\n55555")


def pattern(num):
    rng = range(num, 0, -1)
    lst = [str(i) for i in rng]
    return '\n'.join(''.join(lst[:i]) for i in rng)
