from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)
print(c['x'])  # Выводит 1(из a)
print(c['y'])  # Выводит 2_str(из b)
print(c['z'])  # Выводит 3(из a)

print(len(c))
print(c.keys())
print(c.values())
