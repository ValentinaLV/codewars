"""
https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd

https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a

https://www.codewars.com/kata/5d5ee4c35162d9001af7d699
"""


def paperwork(n, m):
    return n * m if m > 0 and n > 0 else 0


def past(hours, minutes, seconds):
    return (3600 * hours + 60 * minutes + seconds) * 1000


def sum_of_minimums(numbers):
    return sum([min(lst) for lst in numbers])


print(sum_of_minimums([[7, 9, 8, 6, 2], [6, 3, 5, 4, 3], [5, 8, 7, 4, 5]]) == 9)
