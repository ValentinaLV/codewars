def summation(num):
    """
    Write a program that finds the summation of every
    number from 1 to num. The number will
    always be a positive integer greater than 0.
    :param num:
    :return:
    """
    return sum(n for n in range(1, num + 1))


print(summation(8) == 36)


def opposite(number):
    return -number


def find_short(s):
    """
    Simple, given a string of words, return the length of the shortest word(s).
    String will never be empty and you do not need to account for different data types.
    :param s:
    :return:
    """
    return min([len(w) for w in s.split()])


print(find_short("bitcoin take over the world maybe who knows perhaps") == 3)


def comp(array1, array2):
    return None not in (array1, array2) and \
           [n ** 2 for n in sorted(array1)] == sorted(array2)


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
print(comp(a1, a2) == True)


def friend(x):
    return [f for f in x if len(f) == 4]


print(friend(["Ryan", "Kieran", "Mark"]) == ["Ryan", "Mark"])