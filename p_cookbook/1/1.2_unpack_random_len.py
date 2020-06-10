def first_last(grades):
    first, *middle, last = grades
    return sum(middle) / len(middle)


print(first_last([10, 15, 14, 15, 14, 10]))

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phones = record
print(name)
print(email)
print(phones)

records = [('foo', 1, 2),
           ('bar', 'hello'),
           ('foo', 3, 4), ]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for el, *args in records:
    if el == 'foo':
        do_foo(*args)
    if el == 'bar':
        do_bar(*args)
