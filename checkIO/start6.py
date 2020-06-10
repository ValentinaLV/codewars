"""

"""


def nearest_value(values: set, one: int) -> int:
    # your code here
    return min(values, key=lambda num: (abs(one - num), num))


def split_pairs(s):
    # your code here
    # lst = []
    # for i in range(0, len(s)-1, 2):
    #     lst.append(s[i:i + 2])
    # if len(s) % 2 == 0:
    #     return lst
    # lst.append(f'{s[-1]}_')
    # return lst
    s = s + '_' * (len(s) % 2)
    return [s[i:i + 2] for i in range(0, len(s), 2)]


def beginning_zeros(number: str) -> int:
    # your code here
    return len(number) - len(number.lstrip('0'))
    # i = 0
    # while i < len(number) and number[i] == '0':
    #     i += 1
    # return i
    # n = 0
    # for i in number:
    #     if i == "0":
    #         n += 1
    #     else:
    #         break
    # return n


def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    # your code here
    # if text[-1] != '.':
    #     return text[0].upper() + text[1:] + '.'
    # return text[0].upper() + text[1:]
    return f"{text[0].upper()}{text[1:].rstrip('.')}."


def max_digit(number: int) -> int:
    # your code here
    return int(sorted(str(number))[-1])
    #return int(max(str(number)))

    # max = 0
    # while number / 10 > 0:
    #     n = number % 10
    #     if n > max:
    #         max = n
    #     number = number // 10
    # return max


if __name__ == '__main__':
    # print("Example:")
    # print(nearest_value({0, -2}, -1))
    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    # assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    # assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    # assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    # assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    # assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    # assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    # assert nearest_value({-1, 2, 3}, 0) == -1
    # print("Coding complete? Click 'Check' to earn cool rewards!")
    # print("Example:")
    # print(list(split_pairs('abcdf')))
    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert list(split_pairs('abcd')) == ['ab', 'cd']
    # assert list(split_pairs('abc')) == ['ab', 'c_']
    # assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    # assert list(split_pairs('a')) == ['a_']
    # assert list(split_pairs('')) == []
    # print("Coding complete? Click 'Check' to earn cool rewards!")

    # print("Example:")
    # print(correct_sentence("welcome to New York"))

    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert correct_sentence("greetings, friends") == "Greetings, friends."
    # assert correct_sentence("Greetings, friends") == "Greetings, friends."
    # assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    # assert correct_sentence("hi") == "Hi."
    # assert correct_sentence("welcome to New York") == "Welcome to New York."
    #
    # print("Coding complete? Click 'Check' to earn cool rewards!")

    # print("Example:")
    # print(beginning_zeros('0000'))
    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert beginning_zeros('100') == 0
    # assert beginning_zeros('001') == 2
    # assert beginning_zeros('100100') == 0
    # assert beginning_zeros('001001') == 2
    # assert beginning_zeros('012345679') == 1
    # assert beginning_zeros('0000') == 4
    # print("Coding complete? Click 'Check' to earn cool rewards!")

    print("Example:")
    print(max_digit(52))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert max_digit(0) == 0
    assert max_digit(52) == 5
    assert max_digit(634) == 6
    assert max_digit(1) == 1
    assert max_digit(10000) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")

