"""
https://book.pythontips.com/en/latest/map_filter.html
map(function_to_apply, list_of_inputs)

https://www.w3schools.com/python/ref_func_map.asp
"""

items = [1, 2, 3, 4, 5]
squared = []
for el in items:
    squared.append(el ** 2)
print(squared)  # [1, 4, 9, 16, 25]

squared_map = list(map(lambda n: n ** 2, items))
# or
trip_map2 = [x ** 3 for x in items]
print(squared_map)
print(trip_map2)

# from str to int
items_str = ['1', '2', '3', '4', '5']
items_int = list(map(lambda n: int(n), items_str))
print(items_int)


def multiply(x):
    return x * x


def add(x):
    return x + x


funcs = [multiply, add]

for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

lst = ['apple', 'banana', 'cherry']
lst2 = ['orange', 'lemon', 'pineapple']
lst_len = list(map(lambda s: len(s), lst))
print(lst_len)

lst_union = list(map(lambda a, b: f'{a} {b}', lst, lst2))
print(lst_union)

lst5 = [10, 20, 30, 40, 50]
lst_square = list(map(multiply, lst5))
# or
lst_square2 = [x * x for x in lst5]
print(lst_square)
print(lst_square2)


def map(func, iterable):
    for i in iterable:
        yield func(i)

