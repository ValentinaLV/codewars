"""
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""

thistuple = ("apple", "banana", "cherry")

# Access Tuple Items
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:5])
print(thistuple[-4:-1])

# Change Tuple Values
x = ("apple", "banana", "cherry")
print(x)
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Loop Through a Tuple
for x in thistuple:
    print(x)

# Check if Item Exists
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Tuple Length
print(len(thistuple))

# Add Items
# thistuple = ("apple", "banana", "cherry")
# thistuple[3] = "orange" # This will raise an TypeError
# print(thistuple)

# Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Remove Items
# You cannot remove items in a tuple.

# Delete tuple
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists

# Join Two Tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

# count()
tuple4 = ("apple", "banana", "cherry", "cherry")
print(tuple4.count("cherry"))

# index()
print(tuple4.index("cherry", 3))
