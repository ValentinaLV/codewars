"""
https://www.codewars.com/kata/57fe50d000d05166720000b1
https://www.codewars.com/kata/54b45c37041df0caf800020f
"""

from collections import Counter


def sabb(s, value, happiness):
    counter = Counter(s.lower())
    score = value + happiness + sum(counter[c] for c in set("sabbatical"))
    return "Sabbatical! Boom!" if score > 22 else "Back to your desk, boy."


def binary_gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return format(num1, 'b').count('1')
