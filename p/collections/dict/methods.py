"""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and values
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""

car_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Accessing Items
print(car_dict["brand"])
print(car_dict["model"])
print(car_dict["year"])

print(car_dict.get("model"))
print(car_dict.get("models", "no such key"))

# Change Values
car_dict["year"] = 2020
print(car_dict.get("year"))

# Loop Through a Dictionary
for k, v in car_dict.items():
    print('key: {}, value: {}'.format(k, v))

for el in car_dict:
    print(f'key: {el}')

for k in car_dict.keys():
    print(f'key using .keys: {k}')

for el in car_dict:
    print(f'value: {car_dict[el]}')

for v in car_dict.values():
    print(f'value using .values: {v}')

# Check if Key Exists
if 'model' in car_dict:
    print('model is a car_dict key')

# Dictionary Length
print(len(car_dict))

# Adding Items
car_dict['color'] = 'yellow'
print(car_dict)

car_dict.update({'wheels': 'Rosava'})
print(car_dict)

# Removing Items
# => method removes the item with the specified key name
car_dict.pop("color")
print(car_dict)

# => del keyword removes the item with the specified key name
del car_dict["model"]
print(car_dict)

# popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
car_dict.popitem()
print(car_dict)

# Delete dict
# The del keyword can also delete the dictionary completely
# del car_dict
# print(car_dict)  # NameError: name 'car_dict' is not defined

# Clear Dict
# The clear() keyword empties the dictionary:
car_dict.clear()
print(car_dict)  # {}

# Copy a Dictionary
this_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
my_dict = this_dict.copy()
print(my_dict)
this_dict["year"] = 2020
print(my_dict)

# Make a copy of a dictionary with the dict() method:
my_dict2 = dict(this_dict)
print(my_dict2)

# Nested Dictionaries
my_family = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
for k in my_family:
    for k, v in my_family[k].items():
        print(f'k: {k}, v: {v}')

# The dict() Constructor
this_dict3 = dict(brand="Ford", model="Mustang", year=1964)
print(this_dict3)

# setdefault
# The setdefault() method returns the value of the item with the specified key.
# If the key does not exist, insert the key, with the specified value, see example below:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.setdefault('models', 'Bronco')
print(x)  # Bronco

# fromkeys
# Create a dictionary with 3 keys, all with the value 0:
x = ('key1', 'key2', 'key3')
y = 0
this_dict4 = dict.fromkeys(x, y)
print(this_dict4)  # {'key1': 0, 'key2': 0, 'key3': 0}
