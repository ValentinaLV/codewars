"""
https://www.w3schools.com/python/ref_func_all.asp
"""

mylist = [True, True, True]
print(all(mylist))  # True

# Check if all items in a list are True:
lst = [0, 1, 1]
print(all(lst))  # False

# Check if all items in a tuple are True:
tup = (0, True, False)
print(all(tup))  # False

# Check if all items in a set are True:
setik = {0, 1, 0}
print(all(setik))  # False

# Check if all items in a dictionary are True:
dictik = {0: "Apple", 1: "Orange"}
print(all(dictik))  # False
