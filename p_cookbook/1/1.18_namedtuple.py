from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber(addr='tina.lysenok@gmail.com', joined='10-06-2020')

print(sub)
print(sub.addr)
print(sub.joined)

# >>> s = Stock('ACME', 100, 123.45)
# >>> s
# Stock(name='ACME', shares=100, price=123.45)
# >>> s.shares = 75
# Traceback (most recent call last): File "<stdin>", line 1, in <module>
# AttributeError: can't set attribute

# >>> s = s._replace(shares=75)
# >>> s
# Stock(name='ACME', shares=75, price=123.45)

