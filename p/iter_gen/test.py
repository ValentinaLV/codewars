def countdown_iter(num):
    lst = []
    while num != 0:
        lst.append(num)
        num -= 1
    return lst


def countdown_gen(num):
    while num != 0:
        yield num
        num -= 1


print(countdown_iter(10))
result = countdown_gen(10)
print(result)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
# print(next(result)) -> StopIteration


t = ([1, 2, 4], 6, 7)

t[0][1] = 10
print(t)