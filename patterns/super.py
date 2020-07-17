class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def short_name(self):
        return f'{self.first_name[0].upper()}. {self.last_name}'


class FullName(Name):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.full_name = f'{first_name} {last_name}'

    def short_name(self):
        super(FullName, self).short_name()


full_name = FullName('Tina', 'Lysenok')
print(full_name.full_name)
print(full_name.short_name())


class A:
    def __init__(self):
        print('class A')


class B:
    def __init__(self):
        print('class B')


class C(A, B):
    def __init__(self):
        super(A, self).__init__()
        # super().__init__()
        print('class C')

    def __str__(self):
        return 'Hi'


c = C()
print(c)


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        # face_area = super(Square, self).area()
        face_area = super().area()
        return face_area * self.length


square = Square(5)
print(square.area())

cube = Cube(5)
print(cube.surface_area())


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        """
        Luckily, you have some control over how the MRO is constructed.
        Just by changing the signature of the RightPyramid class,
        you can search in the order you want, and the methods will resolve correctly:
        :param base:
        :param slant_height:
        """
        self.base = base  # first length
        self.slant_height = slant_height
        super().__init__(base)  # second length parameter for are() in Square|Rectangle -> base_area here

    def area(self):
        base_area = super().area()
        print(base_area)  # (10*10) => 100
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area


rp = RightPyramid(10, 10)
print(rp.area())
print(RightPyramid.mro())  # [<class '__main__.RightPyramid'>, <class '__main__.Square'>,
# <class '__main__.Rectangle'>, <class '__main__.Triangle'>, <class 'object'>]
