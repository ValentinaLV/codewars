"""
https://www.codewars.com/kata/55e6f5e58f7817808e00002e

https://www.codewars.com/kata/5cc70653658d6f002ab170b5
"""


def seven(num):
    counter = 0
    while num > 99:
        num = num // 10 - 2 * (num % 10)
        counter += 1
    return num, counter
