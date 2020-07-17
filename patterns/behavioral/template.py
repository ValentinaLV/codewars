# http://34.212.143.74/s201911/pycon2019/docs/design_patterns.html#_observer_pattern
from abc import ABC, abstractmethod


class AverageCalculator(ABC):

    def average(self):
        try:
            num_items = 0
            total_sum = 0
            while self.has_next():
                total_sum += self.next_item()
                num_items += 1
            if num_items == 0:
                raise RuntimeError("Can't compute the average of zero items.")
            return total_sum / num_items
        finally:
            self.dispose()

    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next_item(self):
        pass

    def dispose(self):
        pass


class FileAverageCalculator(AverageCalculator):

    def __init__(self, file):
        self.file = file
        self.last_line = self.file.readline()

    def has_next(self):
        return self.last_line != ''

    def next_item(self):
        result = float(self.last_line)
        self.last_line = self.file.readline()
        return result

    def dispose(self):
        self.file.close()


class MemoryAverageCalculator(AverageCalculator):
    def __init__(self, lst):
        self.it = iter(lst)
        self._next = None
        self._has_next = None

    def __iter__(self):
        return self

    def has_next(self):
        if self._has_next is None:
            try:
                self._next = next(self.it)
            except StopIteration:
                self._has_next = False
            else:
                self._has_next = True
        return self._has_next

    def next_item(self):
        if self._has_next:
            result = self._next
        else:
            result = next(self.it)
        self._has_next = None
        return result


fac = FileAverageCalculator(open('data.txt'))
print(fac.average())  # Call the template method

mac = MemoryAverageCalculator([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
print(mac.average())  # Call the template method
