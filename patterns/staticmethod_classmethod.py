import math


class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


my_class = MyClass()
print(my_class.method())  # ('instance method called', <__main__.MyClass object at 0x106f05358>)
print(my_class.classmethod())  # ('class method called', <class '__main__.MyClass'>)
print(my_class.staticmethod())  # static method called
print(MyClass.staticmethod())  # static method called


class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @classmethod
    def margarita(cls):
        return cls(30, ['mozzarella', 'tomatoes']), cls

    @classmethod
    def prosciutto(cls):
        return cls(30, ['mozzarella', 'tomatoes', 'ham']), cls

    @staticmethod
    def circle_area(r):
        """docstring"""
        return r ** 2 * math.pi


pizza = Pizza(30, ['standard'])
print(pizza.margarita())
print(pizza.prosciutto())
print(Pizza.circle_area(100))
print(Pizza.margarita())


def circle_area_test(r):
    """
    docstring
    :param r:
    :return:
    """
    return r ** 2 * math.pi


print(circle_area_test.__doc__)
help(circle_area_test)