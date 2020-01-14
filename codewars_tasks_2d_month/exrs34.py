"""
https://www.codewars.com/kata/5a523566b3bfa84c2e00010b

https://www.codewars.com/kata/5e0f6a3a2964c800238ca87d
"""


def min_sum(lst):
    total = 0
    while len(lst) > 0:
        total += max(lst) * min(lst)
        lst.remove(max(lst))
        lst.remove(min(lst))
    return total


print(min_sum([5, 4, 2, 3]) == 22)
print(min_sum([12, 6, 10, 26, 3, 24]) == 342)
print(min_sum([9, 2, 8, 7, 5, 4, 0, 6]) == 74)


def blocks(s):
    return


print(blocks("21AxBz") == "xzAB12")
print(blocks("abacad") == "abcd-a-a")
print(blocks("") == "")

print(''.join(reversed("21AxBz")))
print("21AxBz"[::-1])














