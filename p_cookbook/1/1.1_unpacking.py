# unpacking

t = (4, 5)
x, y = t
print(x)
print(y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, (year, mon, day) = data
print(year)
print(mon)
print(day)

s = 'Hello'
a, b, c, d, e = s
print(a)
print(b)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares2, price2, _ = data
print(shares2)
print(price2)
