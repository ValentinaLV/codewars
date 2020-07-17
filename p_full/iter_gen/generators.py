jack = {
    "name": "Jack",
    "car": "bmw"
}

john = {
    "name": "John",
    "car": "audi"
}

elsa = {
    "name": "Elsa"
}

users = [jack, john, elsa]
# антипаттерн
# cars = [person["car"] for person in users]
# print(cars)   # ['bmw', 'audi']

# or
# cars2 = []
# for person in users:
#     cars2.append(person['car'])

# print(cars2)  # ['bmw', 'audi']

new_cars = [person.get("car", "") for person in users]
print(new_cars)  # ['bmw', 'audi', '']


def countdown_gen(num):
    while num >= 0:
        yield num
        num -= 1


# print(countdown_gen(10))
# gen = countdown_gen(10)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


def countdown_iter(num):
    lst = []
    while num >= 0:
        lst.append(num)
        num -= 1
    return lst


print(countdown_iter(10))


def odds_nums():
    start = 1
    while True:
        yield start
        start += 2


odd = odds_nums()

for odd in range(10):
    print(next(odd))


def odds_gen2(num):
    start = 1
    while num > 0:
        yield start
        start += 2
        num -= 1

odd_num = odds_gen2(10)
# print(next(odd_num))
# print(next(odd_num))
# print(next(odd_num))
# print(next(odd_num))
# print(next(odd_num))


# def  gen() :
#     i = 0 
#     while True: 
#         yield i 
#         i += 2_str 
#
# x = gen()
#      for i in range(10): 
#         next(x)

def even_nums():
    start = 0
    while True:
        yield start
        start += 2


enen_num = even_nums()

for even_num in range(10):
    print(next(enen_num))


def even_nums2(num):
    start = 0
    while num > 0:
        yield start
        start += 2
        num -= 1


# enen_num2 = even_nums2(5)
# print(next(enen_num2))
# print(next(enen_num2))
# print(next(enen_num2))
# print(next(enen_num2))
# print(next(enen_num2))