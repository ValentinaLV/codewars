class Parent:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name


parent = Parent('Ember', 'Jones')


# print(parent.__first_name)

class Phone:
    username = "Kate"  # public variable
    __serial_number = "11.22.33"  # private variable
    __how_many_times_turned_on = 0  # private variable

    def call(self):  # public method
        print("Ring-ring!")

    def __turn_on(self):  # private method
        self.__how_many_times_turned_on += 1
        print("Times was turned on: ", self.__how_many_times_turned_on)


phone = Phone()
phone._Phone__turn_on()
phone._Phone__serial_number = '44.22.44'
print(phone._Phone__serial_number)