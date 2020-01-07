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


