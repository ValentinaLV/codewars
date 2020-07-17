from abc import ABC, abstractmethod


class AbstractClassExample(ABC):
    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def do_something(self):
        return 'Why'

    def __str__(self):
        return 'AbstractClassExample'


class DoAdd42(AbstractClassExample):
    def do_something(self):
        return 'DoAdd'


x = DoAdd42(4)
print(x.do_something())
