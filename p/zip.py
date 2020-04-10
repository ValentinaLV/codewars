a = [('x', 3), ('y', 4), ('z', 5)]

c = ('x', 'y', 'z', 'm')
v = (3, 4, 5)

print(list(zip(c, v)))
print(list(zip(c[2:] + c[:2], v)))
