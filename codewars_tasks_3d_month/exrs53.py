"""
https://www.codewars.com/kata/5d50e3914861a500121e1958/sql

https://www.codewars.com/kata/5966ec8e62d030d8530000a7
"""


def super_sum(dimension_arr, len_arr):
    return len_arr ** dimension_arr * (len_arr - 1) * dimension_arr // 2
