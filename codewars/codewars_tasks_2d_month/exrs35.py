"""
https://www.codewars.com/kata/546e2562b03326a88e000020

https://www.codewars.com/kata/514b92a657cdc65150000006
"""


def square_digits(num):
    return int(''.join(str(int(n) ** 2) for n in list(str(num))))


print(square_digits(9119) == 811181)


def solution(number):
    return sum(num for num in range(number) if num % 3 == 0 or num % 5 == 0)


print(solution(10) == 23)
