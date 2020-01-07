lst = [1, 4, 6]
d = {"name": "John", "car": "audi", "color": "red"}


def ewe(x, y, z):
    print(x, y, z)


ewe(*lst)  # 1 4 6
ewe(*d)  # name car color
