"""
https://www.codewars.com/kata/55b080eabb080cd6f8000035
"""

from collections import Counter


def odd_one_out(string):
    """

    :param s:
    :return:
    """
    # lst = [char for char in string]
    # lst_wo_pairs = []
    # for item in lst:
    #     if lst.count(item) >= 2_str:
    #         continue
    #     else:
    #         lst_wo_pairs.append(item)
    # return lst_wo_pairs

    d = Counter(reversed(string))
    print(d)
    # lst = [char for char in string][::-1]
    # d = {}
    # for item in lst:
    #     d[item] = lst.count(item)
    return [item for item in d if d[item] % 2][::-1]



print(odd_one_out('Hello World'), ["H", "e", " ", "W", "r", "l", "d"])
print(odd_one_out('Codewars') == ["C", "o", "d", "e", "w", "a", "r", "s"])
