def fib(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(9))


def fib2(n):
    num1, num2 = 0, 1
    for i in range(n - 1):
        num1, num2 = num2, num1 + num2
    return num1


print(fib(2))


def fib_wo_recurs(n):
    n1, n2 = 0, 1
    count = 0
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        while count < n:
            print(n1)
            nth = n1 + n2
            n1, n2 = n2, nth
            count += 1


fib_wo_recurs(9)


def factorial(n):
    num = 1
    while n >= 1:
        num *= n
        n -= 1
    return num


print(factorial(5))


def bsort(lst):
    """
    Write a program in Python to execute the Bubble sort algorithm
    :return:
    """
    for x in range(len(lst) - 1):
        for y in range(len(lst) - 1 - x):
            if lst[y] > lst[y + 1]:
                lst[y], lst[y + 1] = lst[y + 1], lst[y]
    return lst


print(bsort([33, 5, -16]))


def triangle(r):
    for el in range(r):
        print(' ' * (r - el - 1) + '*' * (2 * el + 1))


triangle(9)

import math


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i:
            return True
    return False


print(is_prime(5))


def is_odd_or_even(num):
    return 'Odd' if num % 2 else 'Even'


print(is_odd_or_even(8))


def is_palindrome(string):
    return string == string[::-1]


print(is_palindrome('323'))


# with open(SOME_LARGE_FILE) as fh:
#     count = 0
#     text = fh.read()
#     for character in text:
#         if character.isupper():
#             count += 1

def simple_sort(lst):
    lst_to_int = [int(n) for n in lst]
    lst_to_int.sort()
    return lst_to_int


print(simple_sort(["1", "4", "0", "6", "9"]))

print(list(map(lambda x: int(x), ["1", "4", "0", "6", "9"])))

d = {n: n ** 2 for n in range(10)}
print(d)

d2 = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
d3 = {k: v / 2 for (k, v) in d2.items()}
print(d3)

def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())