"""
https://www.codewars.com/kata/5878520d52628a092f0002d0/train/python

"""


def string_transformer(s):
    """
    String transformer
    "Example Input" ==> "iNPUT eXAMPLE"
    :param s:
    :return:
    """
    # ns = ""
    # for char in s:
    #     if char in ascii_uppercase:
    #         ns += char.lower()
    #     elif char in ascii_lowercase:
    #         ns += char.upper()
    # return ns
    return ' '.join(s.swapcase().split(' ')[::-1])


print(string_transformer("Example Input") == "iNPUT eXAMPLE")


def solution(n):
    """
    Round by 0.5 steps
    :param n:
    :return:
    """
    return round(2 * n) / 2


print(solution(4.2) == 4)
print(solution(4.25) == 4.5)
print(solution(4.4) == 4.5)
print(solution(4.6) == 4.5)
print(solution(4.75) == 5)
print(solution(4.8) == 5)
