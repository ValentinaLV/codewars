"""
Reverser:
Impliment the reverse function, which takes in input n and reverses it. For instance, reverse(123) should return 321.
You should do this without converting the inputted number into a string.

Recursive Replication:
You need to design a recursive function called replicate which will receive arguments times and number.
The function should return an array containing repetitions of the number argument. For instance,
replicate(3, 5) should return [5,5,5].
If the times argument is negative, return an empty array.
As tempting as it may seem, do not use loops to solve this problem.
"""


def reverse(num):  # work with positive and negative nums
    """Returns n with all digits reversed. Assume positive n."""
    sign = num // abs(num)
    num = abs(num)
    rev_int = 0
    while num > 0:
        curr = num % 10
        rev_int = (rev_int * 10) + curr
        num = num // 10
    return rev_int * sign


def reverse2(n):  # work only with positive nums
    m = 0
    while n > 0:
        n, m = n // 10, m * 10 + n % 10
    return m


# print(reverse(-1234))
# print(reverse(1234) == 4321)
# print(reverse(10987) == 78901)
# print(reverse(1020) == 201)


def replicate(times, number):
    if times > 0:
        result = replicate(times - 1, number)
        result.append(number)
        return result
    return []


def replicate2(times, number):
    if times > 0:
        result = replicate(times - 1, number)
        result.append(number)
        return result
    return []


def replicate3(times, number):
    result = []
    while times > 0:
        result.append(number)
        times -= 1
    return result


print(replicate(3, 5))
print(replicate(3, 5) == [5, 5, 5])
print(replicate(5, 1) == [1, 1, 1, 1, 1])
print(replicate(0, 12) == [])
print(replicate(-1, 12) == [])
print(replicate(8, 0) == [0, 0, 0, 0, 0, 0, 0, 0])
