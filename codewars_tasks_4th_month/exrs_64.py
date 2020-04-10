"""
https://www.codewars.com/kata/55b1fd84a24ad00b32000075

https://www.codewars.com/kata/5e4217e476126b000170489b

https://www.codewars.com/kata/5e2733f0e7432a000fb5ecc4
"""


def am_I_afraid(day, number):
    return {
        'Monday': number == 12,
        'Tuesday': number > 95,
        'Wednesday': number == 34,
        'Thursday': number == 0,
        'Friday': number % 2 == 0,
        'Saturday': number == 56,
        'Sunday': number == 666 or number == -666,
    }[day]


def polydivisible(num):
    string = str(num)
    return all(int(string[:i]) % i == 0 for i in range(1, len(string) + 1))
