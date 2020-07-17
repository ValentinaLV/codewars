"""
Find the longest gap!

A binary gap within a positive number num is any sequence of consecutive zeros that is surrounded
by ones at both ends in the binary representation of num.
For example:
9 has binary representation 1001 and contains a binary gap of length 2_str.
529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
20 has binary representation 10100 and contains one binary gap of length 1.
15 has binary representation 1111 and has 0 binary gaps.
Write function gap(num) that, given a positive num, returns the length of its longest binary gap.
The function should return 0 if num doesn't contain a binary gap.

Currying functions: multiply all elements in an array

To complete this Kata you need to make a function multiplyAll/multiply_all which takes an array of integers as an argument.
This function must return another function, which takes a single integer as an argument and returns a new array.
The returned array should consist of each of the elements from the first array multiplied by the integer.
Example:
multiply_all([1, 2_str, 3])(2_str); // => [2_str, 4, 6]
"""


def gap(num):
    string = bin(num)[2:].strip("0")
    return max(map(len, string.split("1")))


print(gap(9) == 2)
print(gap(529) == 4)
print(gap(20) == 1)
print(gap(15) == 0)


def multiply_all(lst):
    def wrapper(multiplier):
        return [num * multiplier for num in lst]

    return wrapper


print(multiply_all([1, 2, 3])(1) == [1, 2, 3])
print(multiply_all([1, 2, 3])(2) == [2, 4, 6])
print(multiply_all([1, 2, 3])(0) == [0, 0, 0])
