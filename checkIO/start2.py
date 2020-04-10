"""

"""


def checkio(lst):
    """
        sums even-indexes elements and multiply at the last
    """
    if lst:
        return sum([num for i, num in enumerate(lst) if i % 2 == 0]) * lst[-1]
    return 0


def left_join(phrases: tuple) -> str:
    """
        Join strings and replace "right" to "left"
    """
    return ','.join(phrases).replace('right', 'left')


import string


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    punctuation = [',', '.', ' ']
    # your code here
    for c in text:
        if c in punctuation:
            return text.split(c)[0].replace(c, '')
    return text.split()[0]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    # assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    # assert checkio([6]) == 36, "(6)*6=36"
    # assert checkio([]) == 0, "An empty array = 0"
    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    # assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    # assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    # assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

    print("Example:")
    print(first_word("... and so on ..."))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
