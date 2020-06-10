mylist = [1, 4, -5, 10, -7, 2, 3, -1]
# list comprehension
greater_zero = [item for item in mylist if item > 0]
print(greater_zero)

# generator
greater_zero2 = (n for n in mylist if n > 0)
print(greater_zero2)

for el in greater_zero2:
    print(el)

# for other values
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(num):
    try:
        n = int(num)
        return True
    except ValueError:
        return False


greater_zero3 = list(filter(is_int, values))
print(greater_zero3)

remove_negative = [n if n > 0 else 0 for n in mylist]
print(remove_negative)

# itertools
addresses = ['5412 N CLARK',
             '5148 N CLARK',
             '5800 E 58TH',
             '2122 N CLARK'
             '5645 N RAVENSWOOD',
             '1060 W ADDISON',
             '4801 N BROADWAY',
             '1039 W GRANVILLE',
             ]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress
more5 = [n > 5 for n in counts]
print(more5)  # [False, False, True, False, False, True, True, False]
lst_compress = list(compress(addresses, more5))
print(lst_compress)
