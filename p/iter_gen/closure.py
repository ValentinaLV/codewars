# все переменные это ссылки на объекты

a = 1
b = a
# 1 obj (a and b has the link on the same obj) and 2 vars
print(id(b))
print(id(a))

a = 2  # создали новую ссылку на новый объект
print(b)  # 1

a = []  # создали новую ссылку на новый объект
b = a  # присвоили эту ссылку в b
a.append('wdwd')
print(b)  # ['wdwd']


def one():
    ### start closure
    x = ['one', 'two']

    def inner():
        print(x)
        print(id(x))

    ### end closure
    return inner


o = one()
o()  # ['one', 'two']
# 4448442376


print(o.__closure__[0].cell_contents)
print(id(o.__closure__[0].cell_contents))  # 4440410056
