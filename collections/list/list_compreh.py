"""
list_variable = [x for x in iterable]
"""
from functools import reduce

lst = [x**2 for x in range(10)]
print(lst)
lst_odd = [num for num in lst if num % 2]
print(lst_odd)
lst_even = [num for num in lst if num % 2 == 0]
print(lst_even)

# list comprehension vs map + filter
# 1
kilometer = [39.2, 36.5, 37.3, 37.8]
feet = list(map(lambda x: float(3280.8399)*x, kilometer))
print(feet)
feet = list(map(int, feet))
print(feet)
uneven = list(filter(lambda x: x % 2, feet))
print(uneven)
even = list(filter(lambda x: x % 2 == 0, feet))
print(even)
# 2
feet2 = [x*float(3280.8399) for x in kilometer]
print(feet2)
feet2 = [int(x) for x in feet2]
print(feet2)
uneven = [x % 2 for x in feet2]
print(uneven)
uneven2 = [x for x in feet2 if x % 2]
print(uneven2)
even1 = [x % 2 == 0 for x in feet2]
print(even1)
even2 = [x for x in feet2 if x % 2 == 0]
print(even2)

# list comprehension vs reduce
# 1
f = [128608, 119750, 122375, 124015]
reduced_feet = reduce(lambda x, y: x+y, feet)
print(reduced_feet)
# 2
reduced_feet2 = sum(x for x in f)
print(reduced_feet2)

# List Comprehensions with Conditionals
even_list = [x / 2 for x in range(25) if x % 2]
print(even_list)
even_list = [x / 2 for x in range(25) if x % 2 == 0]
print(even_list)

divided = [x for x in range(100) if x % 2 == 0 if x % 6 == 0]
print(divided)

# divided = []
# for x in range(100):
#     if x%2 == 0 :
#         if x%6 == 0:
#             divided.append(x)

# If-Else Conditions
f2 = [128, 119, 122, 124]
result = [x + 1 if x > 120 else x + 5 for x in f2]
print(result)
