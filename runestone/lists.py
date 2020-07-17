"""
1 - Create a list called myList with the following six items: 76, 92.3,
“hello”, True, 4, 76. Do it with both append and with concatenation,
one item at a time.
"""

my_list = [76, 92.3, "hello", True, 4, 76]

"""
2_str - Append “apple” and 76 to the list.
Insert the value “cat” at position 3.
Insert the value 99 at the start of the list.
Find the index of “hello”.
Count the number of 76s in the list.
Remove the first occurrence of 76 from the list.
Remove True from the list using pop and index.
"""

my_list.append("apple")
my_list.insert(3, "cat")
my_list.insert(0, 99)
my_list.index("hello")
my_list.count(76)
my_list.remove(76)
my_list.pop(my_list.index(True))

"""
3 - Write a Python function that will take a the list of 100 random 
integers between 0 and 1000 and return the maximum value. (Note: 
there is a builtin function named max but pretend you cannot use it.)
"""
from functools import reduce
from random import randint

max_val = reduce(lambda x, y: x if x > y else y, [randint(0, 1000) for i in range(100)])
print(max_val)

"""
4 - Create a list containing 100 random integers between 0 and 1000 
(use iteration, append, and the random module). Write a function 
called average that will take the list as a parameter and return the average.
"""

l = [randint(0, 1000) for n in range(100)]


def average(lst):
    return sum(lst) / len(lst)


print(average(l))

"""
5 - Write a function sum_of_squares(xs) that computes the sum of the 
squares of the numbers in the list xs. For example, sum_of_squares([2_str, 3, 4]) 
should return 4+9+16 which is 29:
"""


def sum_of_squares(lst):
    return sum(n ** 2 for n in lst)


print(sum_of_squares([2, 3, 4]))

"""
6 - Write a function to count how many odd numbers are in a list.
"""


def count_odd_nums(lst):
    return len([n for n in lst if n % 2])


def count_odd_nums2(lst):
    return len(list(filter(lambda x: x % 2, lst)))


print(count_odd_nums2([2, 3, 4]))

"""
7 - Sum up all the even numbers in a list.
"""


def sum_even_nums(lst):
    return sum(n for n in lst if n % 2 == 0)


def sum_even_nums2(lst):
    return sum(list(filter(lambda x: x % 2 == 0, lst)))


print(sum_even_nums2([2, 3, 4]))

"""
8 - Sum up all the negative numbers in a list.
"""


def sum_negative_nums(lst):
    return sum(n for n in lst if n < 0)


def sum_negative_nums2(lst):
    return sum(list(filter(lambda x: x < 0, lst)))


print(sum_negative_nums2([-2, -3, 4, -5]))

"""
9 - Count how many words in a list have length 5.
"""
words = ["apple", "hello", "banana", "me"]


def count_words(lst):
    return len([w for w in lst if len(w) == 5])


def count_words2(lst):
    return len(list(filter(lambda x: len(x) == 5, lst)))


print(count_words2(words))

"""
10 - Sum all the elements in a list up to but not including the first even number.
"""


def sum_el(lst):
    return sum(n for n in [x for x in lst if x % 2 == 0][1:])


def sum_el2(lst):
    return reduce(lambda x, y: x + y, list(filter(lambda x: x % 2 == 0, lst))[1:])


print(sum_el([2, 4, 5, 6, 2]))

"""
11 - Count how many words occur in a list up to and including the first occurrence of the word “sam”.
"""
lst = ["apple", "hello", "banana", "me", "sam", "banana"]


def count_occur(lst):
    count = 0
    for w in lst:
        count += 1
        if w == "sam":
            break
    return count


print(count_occur(lst))
"""
12 - Write a function replace(s, old, new) that replaces all occurences of old with new in a string s:
"""


def replace(s, old, new):
    sl = s.split(old)  # ["M", "ss", "ss", "pp", " "]
    return new.join(sl)  # "I".join(["M", "ss", "ss", "pp", " "])


if __name__ == "__main__":
    s = 'I love spom! Spom, spom, spom, yum!'
    print(replace('Mississippi', 'i', 'I') == 'MIssIssIppI')
    print(replace(s, 'om', 'am') == 'I love spam! Spam, spam, spam, yum!')
    print(replace(s, 'o', 'a') == 'I lave spam! Spam, spam, spam, yum!')
