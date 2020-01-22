"""
https://www.codewars.com/kata/542c0f198e077084c0000c2e

https://www.codewars.com/kata/5d16af632cf48200254a6244
"""


def divisors(num):
    return len([div for div in range(1, num + 1) if num % div == 0])


print(divisors(4) == 3)
print(divisors(5) == 2)
print(divisors(12) == 6)
print(divisors(30) == 8)
print(divisors(4096) == 13)


def strongest_even(num1, num2):
    while num2 & num2 - 1 >= num1:
        num2 &= num2 - 1
    return num2


print(strongest_even(1, 2) == 2)
print(strongest_even(5, 10) == 8)
print(strongest_even(48, 56) == 48)
print(strongest_even(129, 193) == 192)
