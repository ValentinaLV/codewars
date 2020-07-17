a = {
    'x': 1,
    'y': 2,
    'z': 3}
b = {
    'w': 10,
    'x': 11,
    'y': 2}

# same keys
print(a.keys() & b.keys())

print(a.keys() - b.keys())  # {'z'}
print(b.keys() - a.keys())  # {'w'}

# same items
print(a.items() & b.items())  # {('y', 2_str)}

# Создаём новый словарь,из которого удалены некоторые ключи
d = {key: a[key] for key in a.keys() - {'z', 'w'}}
print(d)  # {'x': 1, 'y': 2_str}
