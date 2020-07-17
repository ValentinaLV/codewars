from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here
    if elements:
        return True if set(elements) == {elements[0]} else False
    return True


from functools import reduce


def checkio(number: int) -> int:
    return reduce(lambda x, y: x * y, [int(n) for n in str(number) if n != '0'])
    # return int(reduce(lambda x, y: int(x)*int(y), list(filter(lambda x: int(x) != 0, str(number)))))


def checkio2(data: list) -> list:
    # Your code here
    # It's main function. Don't remove this function
    # It's used for auto-testing and must return a result for check.

    # replace this for solution
    return [n for n in data if data.count(n) > 1]


def popular_words(text: str, words: list) -> dict:
    # your code here
    return {w: text.lower().split().count(w) for w in words}


def backward_string_by_word(text: str) -> str:
    # your code here
    return ' '.join([c[::-1] for c in text.split(' ')])


def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    return sorted(data, key=lambda x: x['price'], reverse=True)[:limit]


# bigger_price = lambda limit,data: sorted(data, key=lambda x:-x['price'])[:limit]


def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    return text.find(symbol, text.find(symbol) + 1) if text.count(symbol) > 1 else None


from collections import Counter


def frequency_sort(items):
    counts = Counter(items)
    # return sorted(items, key=lambda x: -counts[x])
    # return sorted(items, key=counts.get, reverse=True)
    # return sorted(items, key=items.count, reverse=True)
    # return [n for n, count in Counter(items).most_common() for i in range(count)]
    return sorted(items, key=lambda x: items.index(x))


def frequency_sort2(items):
    popularity = dict(map(lambda x: (x, items.count(x)), items))
    print(popularity)
    # Sort by first appearance in list
    r = sorted(items, key=lambda x: items.index(x))

    # Now resort by popularity, preserving first appearance
    return sorted(r, key=lambda x: popularity[x], reverse=True)


print(frequency_sort2([4, 6, 2, 2, 6, 4, 4, 4]))

if __name__ == '__main__':
    # print("Example:")
    # print(all_the_same([1, 1, 1]))
    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert all_the_same([1, 1, 1]) == True
    # assert all_the_same([1, 2_str, 1]) == False
    # assert all_the_same(['a', 'a', 'a']) == True
    # assert all_the_same([]) == True
    # assert all_the_same([1]) == True
    # print("Coding complete? Click 'Check' to earn cool rewards!")

    # print('Example:')
    # print(checkio(1000))
    #
    # # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert checkio(123405) == 120
    # assert checkio(999) == 729
    # assert checkio(1000) == 1
    # assert checkio(1111) == 1
    # print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

    # print('Example:')
    # print(checkio2([1, 2_str, 3, 1, 3]))
    #
    # assert list(checkio2([1, 2_str, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    # assert list(checkio2([1, 2_str, 3, 4, 5])) == [], "2nd example"
    # assert list(checkio2([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    # assert list(checkio2([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    # print("It is all good. Let's check it now")

    # print("Example:")
    # print(popular_words('''
    # When I was One
    # I had just begun
    # When I was Two
    # I was nearly new
    # ''', ['i', 'was', 'three', 'near']))
    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert popular_words('''
    # When I was One
    # I had just begun
    # When I was Two
    # I was nearly new
    # ''', ['i', 'was', 'three', 'near']) == {
    #     'i': 4,
    #     'was': 3,
    #     'three': 0,
    #     'near': 0
    # }
    # print("Coding complete? Click 'Check' to earn cool rewards!")

    # print("Example:")
    # print(backward_string_by_word('hello   world'))
    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert backward_string_by_word('') == ''
    # assert backward_string_by_word('world') == 'dlrow'
    # assert backward_string_by_word('hello world') == 'olleh dlrow'
    # assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    # assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    # print("Coding complete? Click 'Check' to earn cool rewards!")

    # from pprint import pprint
    #
    # print('Example:')
    # pprint(bigger_price(2_str, [
    #     {"name": "bread", "price": 100},
    #     {"name": "wine", "price": 138},
    #     {"name": "meat", "price": 15},
    #     {"name": "water", "price": 1}
    # ]))

    # These "asserts" using for self-checking and not for auto-testing
    # assert bigger_price(2_str, [
    #     {"name": "bread", "price": 100},
    #     {"name": "wine", "price": 138},
    #     {"name": "meat", "price": 15},
    #     {"name": "water", "price": 1}
    # ]) == [
    #            {"name": "wine", "price": 138},
    #            {"name": "bread", "price": 100}
    #        ], "First"
    #
    # assert bigger_price(1, [
    #     {"name": "pen", "price": 5},
    #     {"name": "whiteboard", "price": 170}
    # ]) == [{"name": "whiteboard", "price": 170}], "Second"
    #
    # print('Done! Looks like it is fine. Go and check it')

    # print('Example:')
    # print(second_index("hi mayor", " "))
    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert second_index("sims", "s") == 3, "First"
    # assert second_index("find the river", "e") == 12, "Second"
    # assert second_index("hi", " ") is None, "Third"
    # assert second_index("hi mayor", " ") is None, "Fourth"
    # assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    # print('You are awesome! All tests are done! Go Check it!')

    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
