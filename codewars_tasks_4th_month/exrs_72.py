"""

https://www.codewars.com/kata/5a905c2157c562994900009d

"""
from functools import reduce


def product_array(nums):
    product = reduce((lambda x, y: x * y), nums)
    return [product / x for x in nums]


def magic(lst):
    new_lst = []
    for i in lst:
        if i % 2:
            new_lst.append(i)
    return new_lst

if __name__ == '__main__':
    test = [[57, 12, 34, 67, 23, 97]]
    for sub_test in test:
        print('{}'.format(magic(sub_test)))

