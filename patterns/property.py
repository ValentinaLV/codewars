# # Python program to explain property() function
#
# # Alphabet class
# class Alphabet:
#     def __init__(self, value):
#         self._value = value
#
#         # getting the values
#
#     def getValue(self):
#         print('Getting value')
#         return self._value
#
#         # setting the values
#
#     def setValue(self, value):
#         print('Setting value to ' + value)
#         self._value = value
#
#         # deleting the values
#
#     def delValue(self):
#         print('Deleting value')
#         del self._value
#
#     value = property(getValue, setValue, delValue, )


class Alphabet:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        print('Getting value')
        return self._value

    @value.setter
    def value(self, value):
        print('Setting value to ' + value)
        self._value = value

    @value.deleter
    def value(self):
        print('Deleting value')
        del self._value


a = Alphabet('Valia')
print(a.value)
a.value = 'Valentyna'
print(a.value)
del a.value
