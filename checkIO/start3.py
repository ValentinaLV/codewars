"""

"""


def sum_numbers(text: str) -> int:
    # your code here
    return sum(int(word) for word in text.split() if word.isdigit())


from itertools import chain

# initializing string
test_list = [1, 4, 5, 6, 7, 3, 5, 9, 2, 4]

# initializing split index list
split_list = [2, 5, 7]

# printing original list
print("The original list is : " + str(test_list))

# printing original split index list
print("The original split index list : " + str(split_list))

# using itertools.chain() + zip()
# to perform custom list split
temp = zip(chain([0], split_list), chain(split_list, [None]))
res = list(test_list[i: j] for i, j in temp)

# printing result
print("The splitted lists are : " + str(res))


def split_list(items: list) -> list:
    # your code here
    # i = math.floor(len(items) / 2)
    # if len(items) % 2 == 0:
    #     temp = zip((0, i), (i, None))
    # else:
    #     temp = zip((0, i + 1), (i + 1, None))
    # return list(items[i: j] for i, j in temp)
    return [items[:(len(items) + 1) // 2], items[(len(items) + 1) // 2:]]


# split_list = lambda items: [items[:(half:=(len(items)+1) // 2)], items[half:]]

import re


def find_quotes(text):
    return re.findall(r'"(.*?)"', text)
    # return text.split('"')[1::2]


if __name__ == '__main__':
    # print("Example:")
    # print(sum_numbers('my numbers is 2'))
    #
    # # These "asserts" are used for self-checking and not for an auto-testing
    # assert sum_numbers('hi') == 0
    # assert sum_numbers('who is 1st here') == 0
    # assert sum_numbers('my numbers is 2') == 2
    # assert sum_numbers('This picture is an oil on canvas '
    #                    'painting by Danish artist Anna '
    #                    'Petersen between 1845 and 1910 year') == 3755
    # assert sum_numbers('5 plus 6 is') == 11
    # assert sum_numbers('') == 0
    # print("Coding complete? Click 'Check' to earn cool rewards!")

    print("Example:")
    print(split_list([1, 2, 3]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")

    print("Example:")
    print(find_quotes('"Lorem Ipsum" is simply dummy text ''of the printing and typesetting '
                      'industry. Lorem Ipsum has been the '
                      '"industry\'s standard dummy text '
                      'ever since the 1500s", when an '
                      'unknown printer took a galley of '
                      'type and scrambled it to make a type '
                      'specimen book. It has survived not '
                      'only five centuries, but also the '
                      'leap into electronic typesetting, '
                      'remaining essentially unchanged. "It '
                      'was popularised in the 1960s" with '
                      'the release of Letraset sheets '
                      'containing Lorem Ipsum passages, and '
                      'more recently with desktop '
                      'publishing software like Aldus '
                      'PageMaker including versions of '
                      'Lorem Ipsum.'))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert find_quotes('"Greetings"') == ['Greetings']
    # assert find_quotes('Hi') == []
    # assert find_quotes('good morning mister "superman"') == ['superman']
    # assert find_quotes('"this" doesn\'t make any "sense"') == ['this', 'sense']
    # assert find_quotes('"Lorem Ipsum" is simply dummy text ''of the printing and typesetting '
    #                    'industry. Lorem Ipsum has been the '
    #                    '"industry\'s standard dummy text '
    #                    'ever since the 1500s", when an '
    #                    'unknown printer took a galley of '
    #                    'type and scrambled it to make a type '
    #                    'specimen book. It has survived not '
    #                    'only five centuries, but also the '
    #                    'leap into electronic typesetting, '
    #                    'remaining essentially unchanged. "It '
    #                    'was popularised in the 1960s" with '
    #                    'the release of Letraset sheets '
    #                    'containing Lorem Ipsum passages, and '
    #                    'more recently with desktop '
    #                    'publishing software like Aldus '
    #                    'PageMaker including versions of '
    #                    'Lorem Ipsum.') == ['Lorem Ipsum',
    #                                        "industry's standard dummy text ever "
    #                                        'since the 1500s',
    #                                        'It was popularised in the 1960s']
    # assert find_quotes('count empty quotes ""') == ['']
    # print("Coding complete? Click 'Check' to earn cool rewards!")
