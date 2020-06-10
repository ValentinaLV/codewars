"""
https://www.codewars.com/kata/52f3149496de55aded000410

https://www.codewars.com/kata/57ee2a1b7b45efcf700001bf
"""


def sum_digits(nums):
    return sum(int(num) for num in str(abs(nums)))


print(sum_digits(10) == 1)
print(sum_digits(99) == 18)
print(sum_digits(-32) == 5)


def cat_mouse(x, steps):
    m, d, c = (x.find(animal) for animal in 'mDC')
    return ('boring without all three' if c < 0 or d < 0 or m < 0 else
            'Escaped!' if abs(c - m) > steps else
            'Protected!' if c < d < m or c > d > m else
            'Caught!')


print(cat_mouse('..D.....C.m', 2) == "Caught!")
print(cat_mouse('............C.............D..m...', 8) == "Escaped!")
print(cat_mouse('m.C...', 5) == "boring without all three")
print(cat_mouse('.CD......m.', 10) == "Protected!")
print(cat_mouse('.CD......m.', 1) == "Escaped!")
