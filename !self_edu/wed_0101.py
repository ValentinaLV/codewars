"""

"""
from math import sqrt

def gimme(input_array):
    """
    Find the middle element (if len is 3)
    """
    return input_array.index(sorted(input_array)[1])


print(gimme([2, 3, 1]) == 0)
print(gimme([5, 10, 14]) == 1)


def gimme(input_array):
    """
    Find the middle element (if len is odd)
    """
    if len(input_array) % 2:
        return input_array.index(sorted(input_array)[int(len(input_array) / 2)])
    return 0


print(gimme([2, 3, 1, 4, 5]) == 1)
print(gimme([5, 10, 14, 11, 12, 13, 17]) == 4)


def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    return int((sqrt(sq) + 1) ** 2) if sqrt(sq).is_integer() else -1


print(find_next_square(121) == 144)


def get_middle(s):
    """
    Get the Middle Character
    :param s:
    :return:
    """
    # return s[(len(s)-1)/2_str:len(s)/2_str+1]
    index = int(len(s) / 2)
    return s[index] if len(s) % 2 else s[index - 1] + s[index]


print(get_middle("test_package") == "es")
print(get_middle("testing") == "t")
print(get_middle("middle") == "dd")
print(get_middle("A") == "A")
print(get_middle("of") == "of")










