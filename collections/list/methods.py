"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""

this_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# Access Items
print(this_list[1])
print(this_list[-1])

# Range of Indexes
print(this_list[2:5])
print(this_list[:4])
print(this_list[4:])
print(this_list[-4:-1])

# Change Item Value
this_list[1] = "blackcurrant"
print(this_list)

# Loop Through a List
for i in this_list:
    print(i)

# Check if Item Exists
if "apple" in this_list:
    print("yes")

# List Length
print(len(this_list))

# Add Items
this_list.append("orange")
this_list.insert(1, "lemon")
# this_list[10] = "peanut"  # IndexError: 10 > len(this_list)
this_list[8] = "peanut"  # 8 == len(this_list)
print(this_list)

# Remove Item
this_list.remove("apple")
print(this_list)
# The pop() method removes the specified index, (or the last item if index is not specified):
this_list.pop()
print(this_list)
this_list.pop(0)
print(this_list)
del this_list[0]
print(this_list)

# Delete list
# The del keyword can also delete the list completely:
# del thislist (NameError)
# thislist.clear() ([])

# Copy a List
"""
You cannot copy a list simply by typing list2 = list1, 
because: list2 will only be a reference to list1, 
and changes made in list1 will automatically also 
be made in list2.
"""
my_list1 = this_list.copy()
my_list2 = this_list[:]
my_list3 = list(this_list)

# Join Two Lists
# 1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
# 2
for el in list2:
    list1.append(el)
print(list1)
# 3
lst2 = ["a", "b", "c"]
lst1 = [1, 2, 3]
lst1.extend(lst2)
print(lst1)

# The list() Constructor
lst_constr = list(("apple", "banana", "cherry"))
print(lst_constr)

# count()
lst = ["apple", "banana", "cherry", "banana", "banana"]
print(lst.count("banana"))

# index()
print(lst.index("banana"))

# reverse()
print(lst.reverse())  # None
print(lst)  # ['banana', 'banana', 'cherry', 'banana', 'apple']
# sort()
print(lst.sort())  # None
print(lst)  # ['apple', 'banana', 'banana', 'banana', 'cherry']
