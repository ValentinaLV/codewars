"""
number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]


"""


def number(lines):
    result = []
    for i, n in enumerate(lines, 1):
        result.append(str(i) + ": " + n)
    return result
    # ['%d: %s' % v for v in enumerate(lines, 1)]


print(number(["a", "b", "c"]))

