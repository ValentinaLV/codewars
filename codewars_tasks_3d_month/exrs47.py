"""
https://www.codewars.com/kata/5a4e3782880385ba68000018

https://www.codewars.com/kata/5a99a03e4a6b34bb3c000124
"""

from gmpy2 import is_prime
from functools import reduce
from operator import mul


def num_primorial(number):
    primes = [n for n in range(100000) if is_prime(n)]
    return reduce(mul, primes[:number])
