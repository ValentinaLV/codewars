def is_all_upper(text: str) -> bool:
    return text.replace(' ', '').isupper()
    # if text:
    #     return all([c.isupper() for c in text])
    # return False
    # return all(map(str.isupper, text.replace(' ', ''))) or bool(text.strip()) is False


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('    '))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

from typing import Iterable


def is_ascending(items: Iterable[int]) -> bool:
    # return False if len(items) > 1 and set(items) == {items[0]} else sorted(items) == items
    return all((items[i] < items[i + 1] for i in range(len(items) - 1)))


if __name__ == '__main__':
    print("Example:")
    print(is_ascending([-5, 10, 99, 123456]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_ascending([-5, 10, 99, 123456]) == True
    assert is_ascending([99]) == True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
    assert is_ascending([]) == True
    assert is_ascending([1, 1, 1, 1]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")


def verify_anagrams(first_word, second_word):
    return sorted(first_word.replace(' ', '').lower()) \
           == sorted(second_word.replace(' ', '').lower())


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    # assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    # assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"


def goes_after(word: str, first: str, second: str) -> bool:
    return (word.find(second) - word.find(first)) == 1


if __name__ == '__main__':
    print("Example:")
    print(goes_after('world', 'w', 'o'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert goes_after('world', 'w', 'o') == True
    assert goes_after('world', 'l', 'o') == False
    assert goes_after('panorama', 'a', 'n') == True
    assert goes_after('list', 'l', 'o') == False
    assert goes_after('', 'l', 'o') == False
    assert goes_after('list', 'l', 'l') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")


def absolute_sorting(numbers_array: tuple) -> list:
    return sorted(numbers_array, key=abs)


# def absolute_sorting(array):
#     array = list(array)
#     for i in range(len(array)-1):
#         for x in range(len(array)-1):
#             if abs(array[x])>abs(array[x+1]):
#                 array[x],array[x+1]=array[x+1],array[x]
#     return array


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(list(absolute_sorting((-20, -5, 10, 15))))


    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)


    assert check_it(absolute_sorting((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(absolute_sorting((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(absolute_sorting((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
