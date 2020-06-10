"""
https://www.codewars.com/kata/5af4119888214326b4000019

https://www.codewars.com/kata/52e9aa89b5acdd26d3000127
Multiply characters
spam(1)  ==> "hue"
spam(6)  ==> "huehuehuehuehuehue"
spam(14) ==> "huehuehuehuehuehuehuehuehuehuehuehuehuehue"
"""


def amidakuji(lst):
    nums = list(range(len(lst[0]) + 1))
    for line in lst:
        for i, swap in enumerate(line):
            if swap == '1':
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


def spam(num):
    return 'hue' * num