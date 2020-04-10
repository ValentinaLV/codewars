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
#cars = [person["car"] for person in users]
#print(cars)   # ['bmw', 'audi']

# or
# cars2 = []
# for person in users:
#     cars2.append(person['car'])

#print(cars2)  # ['bmw', 'audi']

new_cars = [person.get("car", "") for person in users]
print(new_cars)  # ['bmw', 'audi', '']


def countdown_gen(num):
    while num >= 0:
        yield num
        num -= 1


print(countdown_gen(10))
gen = countdown_gen(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


def countdown_iter(num):
    lst = []
    while num >= 0:
        lst.append(num)
        num -= 1
    return lst


print(countdown_iter(10))


def odds_gen(num):
    while num % 0:
        yield num
        num -= 1

#def  gen() :
#     i = 0 
#     while True: 
#         yield i 
#         i += 2 
#
# x = gen()
#      for i in range(10): 
#         next(x)