from abc import ABC, abstractmethod


class PngInterface(ABC):
    @abstractmethod
    def draw(self):
        pass


class PngImage(PngInterface):
    def __init__(self, png):
        self.png = png
        self.format = "raster"

    @staticmethod
    def get_image():
        return 'png'

    def draw(self):
        print("drawing " + self.get_image())


class SvgImage:
    '''
    Оказывается, есть библиотека для работы с векторной графикой,
    которую вы можете использовать вместо того, чтобы реализовывать
    все эти совершенно новые функции самостоятельно.
    Однако классы не соответствуют вашему интерфейсу
    (они не реализуют draw() метод):
    '''

    def __init__(self, svg):
        self.svg = svg
        self.format = "vector"

    @staticmethod
    def get_image():
        return "svg"


class SvgAdapter(PngInterface):
    def __init__(self, svg):
        self.svg = svg

    def rasterize(self):
        return "rasterized " + self.svg.get_image()

    def draw(self):
        img = self.rasterize()
        print("drawing " + img)


regular_png = PngImage('some data')
regular_png.draw()

'''
Адаптер Объект просто оборачивает внешний (услугу) класс, 
предлагая интерфейс , который соответствует нашему 
собственному (клиенту) класс. 
В этом случае сервис предоставляет нам векторную графику, 
а наш адаптер выполняет растеризацию и рисует результирующее 
изображение
'''
example_svg = SvgImage('some data')
adapter = SvgAdapter(example_svg)
adapter.draw()
