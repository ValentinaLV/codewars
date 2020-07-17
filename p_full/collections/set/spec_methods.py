"""
Множество
"""

# 1
# difference() => Returns a set containing the difference between two or more sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
z1 = y.difference(x)
print(z)  # {'banana', 'cherry'}
print(z1)  # {'google', 'microsoft'}

# 2_str
# The difference_update() method removes the items that exist in both sets.
x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "apple"}
x1.difference_update(y1)  # {'cherry', 'banana'}
y1.difference_update(x1)  # {'microsoft', 'google', 'apple'}
print(x1)
print(y1)

"""
The difference_update() method is different from 
the difference() method, because the difference()
method returns a new set, without the unwanted items, 
and the difference_update() method removes the unwanted 
items from the original set.
"""

# 3
# The intersection() method returns a set that contains the similarity between two or more sets.
x2 = {"apple", "banana", "cherry"}
y2 = {"google", "microsoft", "apple"}
z2 = x2.intersection(y2)
z2_ = y2.intersection(x2)
print(z2)  # {'apple'}
print(z2_)  # {'apple'}

# 4
# The intersection_update() method removes the items that is not present in both sets
# (or in all sets if the comparison is done between more than two sets).
x3 = {"apple", "banana", "cherry"}
y3 = {"google", "microsoft", "apple"}
x3.intersection_update(y3)
print(x3)

"""
The intersection_update() method is different from the intersection() method, because 
the intersection() method returns a new set, without the unwanted items, 
and the intersection_update() method removes the unwanted items from 
the original set.
"""

# 5
# The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)  # True / they are completely unique

# 6
# The issubset() method returns True if all items in the set exists in the specified set, otherwise it retuns False.
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)  # True

# 7
# The issuperset() method returns True if all items in the specified set exists in the original set,
# otherwise it returns False.
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issubset(y)
z1 = x.issuperset(y)
print(z)  # False
print(z1)  # True

# 8
# The symmetric_difference() method returns a set that contains all items from both set,
# but not the items that are present in both sets.
# return all diff items
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)  # {'google', 'microsoft', 'banana', 'cherry'}

# 9
# The symmetric_difference_update() method updates the original set by removing items that
# are present in both sets, and inserting the other items.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
y.symmetric_difference_update(x)
print(x)  # {'banana', 'cherry', 'google', 'microsoft'}
print(y)  # {'banana', 'cherry', 'google'}
