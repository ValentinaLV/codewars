"""
https://book.pythontips.com/en/latest/map_filter.html
As the name suggests, filter creates a list of elements for which a function returns true.

https://www.w3schools.com/python/ref_func_filter.asp

https://www.geeksforgeeks.org/filter-in-python/
"""
# ---------1----------
number_list = range(-5, 5)
lst_f = list(filter(lambda x: x < 0, number_list))
print(lst_f)
# or
lst_f2 = [x for x in number_list if x < 0]
print(lst_f2)

# ---------2_str----------
ages = [5, 12, 17, 18, 24, 32]


def check_age(age):
    return True if age > 18 else False


ages_f = list(filter(check_age, ages))
print(ages_f)
# or
ages_f2 = [x for x in ages if x > 18]
print(ages_f2)

# ---------3----------
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p_full', 'r']


def check_letters(letter):
    return True if letter in ['a', 'e', 'i', 'o', 'u'] else False


res = list(filter(check_letters, sequence))
print(res)  # ['e', 'e']
# or
res2 = [l for l in sequence if l in ['a', 'e', 'i', 'o', 'u']]
print(res2)  # ['e', 'e']


# ---------4----------
seq = [0, 1, 2, 3, 5, 8, 13]
seq_odd = list(filter(lambda x: x % 2, seq))
seq_even = list(filter(lambda x: x % 2 == 0, seq))
print(seq_odd)
print(seq_even)
# or
seq_odd1 = [x for x in seq if x % 2]
seq_even1 = [x for x in seq if x % 2 == 0]
print(seq_odd1)
print(seq_even1)




