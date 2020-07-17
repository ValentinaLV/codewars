"""
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
"""
# SETS => {, , ,}
# / unordered
# / unique items
# / can't change items, only delete or add

thisset = {"apple", "banana", "cherry"}

# Access Items
for el in thisset:
    print(el)

print("banana" in thisset)

# Change Items
# Once a set is created, you cannot change its items, but you can add new items.
# every time set rearrange items (every time new index)

# Add Items
thisset.add("lemon")
thisset.update(["orange", "mango", "grapes", "pineapple"])
print(thisset)

# Get the Length of a Set
print(len(thisset))

# Remove Item
# If the item to remove does not exist, remove() will raise an KeyError.
thisset.remove("banana")
print(thisset)
# If the item to remove does not exist, discard() will NOT raise an error.
thisset.discard("banana")
print(thisset)
# pop() method remove an item, but this method will remove the last random item.
# Sets are unordered, so when using the pop() method, you will not know which item that gets removed.
thisset.pop()
print(thisset)

# clear()
thisset2 = {"apple", "banana", "cherry"}
thisset2.clear()
print(thisset2)  # set()

# Delete set
# thisset3 = {"apple", "banana", "cherry"}
# del thisset3
# print(thisset3)  # NameError

# Join Two Sets
# Both union() and update() will exclude any duplicate items.
# 1
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
# 2_str
set11 = {"a", "b", "c"}
set21 = {1, 2, 3}
set11.update(set21)
print(set11)

# The set() Constructor
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)



