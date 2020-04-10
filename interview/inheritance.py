# for multiple inheritance need to add **kwargs
# polymorphism in Python => overwriting (w/o overloading like in Java)


class Shape:
    def __init__(self, x, y, **kwargs):
        self.x = x
        self.y = y
        super.__init__(**kwargs)


class ColoredShape(Shape):
    def __init__(self, x, y, c, **kwargs):
        super().__init__(x, y, **kwargs)
        self.c = c


class ColoredCircle(ColoredShape):
    def __init__(self, x, y, c, r, **kwargs):
        super().__init__(x, y, c, **kwargs)
        self.r = r


class TriangleShape(Shape):
    ...


class ColoredTriangle(ColoredShape, TriangleShape):
    ...


print(ColoredTriangle.mro())
