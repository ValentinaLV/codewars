def is_repdigit(num):
    return True if len(set(str(num))) == 1 else False


print(is_repdigit(-11))


def get_discounts(nums, d):
    """
    get_discounts([2, 4, 6, 11], "50%") ➞ [1, 2, 3, 5.5]
    get_discounts([10, 20, 40, 80], "75%") ➞ [7.5, 15, 30, 60]
    get_discounts([100], "45%") ➞ [45]
    :param nums:
    :param d:
    :return:
    """
    return [n * float(d[:2]) * 0.01 for n in nums]


print(get_discounts([2, 4, 6, 11], "50%"))


def counterpartCharCode(char):
    return ord(char)


print(counterpartCharCode('a'))


def get_student_names(students: dict):
    """
    Create a function that takes a dictionary of students and returns
    a list of student names in alphabetical order.
    :param students:
    :return:
    """
    return sorted(students.values())


def matrix(repeat, count_el, el):
    """
    matrix(3, 2, 3) ➞ [[3, 3], [3, 3], [3, 3]]
    matrix(2, 1, "edabit") ➞ [["edabit"], ["edabit"]]
    matrix(3, 2, 0) ➞ [[0, 0], [0, 0], [0, 0]]
    :param x:
    :param y:
    :param z:
    :return:
    """
    # lst = []
    # for i in range(repeat):
    #     lst.append([el] * count_el)
    # return lst
    return [[el]*count_el for i in range(repeat)]


print(matrix(3, 2, 3))


def is_valid_PIN(pin: str):
    return True if pin.isdigit() and len(pin) == 4 or len(pin) == 6 else False


print(is_valid_PIN('1234'))


def maurice_wins(m_snails, s_snails):
    """
    List 1: [s, m, f] for Maurice.
    List 2: [s, m, f] for Steve.
    Round 1: [s, f] Sacrifice his slowest snail against Steve's fastest.
    Round 2: [m, s] Use his middle snail against Steve's slowest.
    Round 3: [f, m] Use his fastest snail against Steve's middle.
    :param m_snails:
    :param s_snails:
    :return:
    """
    # count_win = 0
    # count_loose = 0
    # fight_lst = [[m_snails[0], s_snails[2]],
    #              [m_snails[1], s_snails[0]],
    #              [m_snails[2]], [s_snails[1]]]
    # for i in fight_lst:
    #     if i[0] > i[1]:
    #         count_win += 1
    #     else:
    #         count_loose += 1
    #
    # return count_win > count_loose
    return sum(m > s for m, s in zip(m_snails, s_snails[2:] + s_snails[:2])) > 1


# m_snails = [1, 8, 20]
# lst = m_snails[1:] + m_snails[:1]
# print(lst)
print(maurice_wins([1, 8, 20], [2, 9, 100]))


def sum_neg(lst):
    """
    Create a function that takes a list of positive and negative numbers.
    Return a list where the first element is the count of positive numbers
    and the second element is the sum of negative numbers.
    sum_neg([92, 6, 73, -77, 81, -90, 99, 8, -85, 34]) ➞ [7, -252]
    Positive Count / Negative Sum
    :param lst:
    :return:
    """
    count_positive = len([num for num in lst if num > 0])
    sum_negative = sum(num for num in lst if num < 0)
    return [count_positive, sum_negative]


def letter_check(lst):
    """
    Are Letters in the Second String Present in the First?
    letter_check(["trances", "nectar"]) ➞ True
    letter_check(["compadres", "DRAPES"]) ➞ True
    letter_check(["parses", "parsecs"]) ➞ False
    :param lst:
    :return:
    """
    return all([char in lst[0].lower() for char in lst[1].lower()])


print(letter_check(["trances", "nectar"]))


def hacker_speak(txt):
    """
    Create a function that takes a string as an argument
    and returns a coded (h4ck3r 5p34k) version of the string.
    hacker_speak("javascript is cool") ➞ "j4v45cr1pt 15 c00l"
    hacker_speak("programming is fun") ➞ "pr0gr4mm1ng 15 fun"
    hacker_speak("become a coder") ➞ "b3c0m3 4 c0d3r"
    :param txt:
    :return:
    """
    d = {'a': '4', 'e': '3', 's': '5', 'o': '0', 'i': '1'}
    lst = []
    for c in txt:
        if c in d.keys():
            lst.append(d[c])
        else:
            lst.append(c)

    return ''.join(lst)

    #return txt.translate(str.maketrans('aeios', '43105'))



print(hacker_speak("programming is fun"))
