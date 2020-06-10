"""

"""


def increment_string(string):
    head = string.rstrip('0123456789')
    tail = string[len(head):]
    if not tail:
        return f"{head}{1}"
    return f"{head}{str(int(tail) + 1).zfill(len(tail))}"


# print(increment_string("foo") == "foo1")
# print(increment_string("foobar001") == "foobar002")
# print(increment_string("foobar1") == "foobar2")
# print(increment_string("foobar00") == "foobar01")
# print(increment_string("foobar99") == "foobar100")


def up_array(lst):
    if not lst or max(lst) > 9 or min(lst) < 0:
        return None
    return [int(num) for num in str(int("".join(map(lambda x: str(x), lst))) + 1)]


# print(up_array([2, 3, 9]), [2, 4, 0])
# print(up_array([4, 3, 2, 5]), [4, 3, 2, 6])
# print(up_array([1, -9]), None)


