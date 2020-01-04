"""
Reduce is a really useful function for performing some computation on a list and returning the result.
https://book.pythontips.com/en/latest/map_filter.html



"""
from functools import reduce
from operator import sub

# ---------1---------
product = 1
lst = [1, 2, 3, 4]

for i in lst:
    product = product * i
print(product)  # 24

# or
res_prod2 = reduce(lambda x, y: x * y, lst)
print(res_prod2)  # 24

# ---------2---------
res_sum = reduce(lambda x, y: x + y, lst)
print(res_sum)

# ---------3---------
max_el = reduce(lambda x, y: x if x > y else y, lst)
print(max_el)

min_el = reduce(lambda x, y: x if x < y else y, lst)
print(min_el)

# ---------4---------
lis = [1, 3, 5, 6, 2]
sub_elemnts = reduce(sub, lis)
print(sub_elemnts)

