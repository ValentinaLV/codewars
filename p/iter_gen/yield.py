def countdown(n):
    res = []
    while n != 0:
        res.append(n - 1)
        n -= 1
    return res


print(countdown(4))  # [3, 2, 1, 0]


def get_countdown(n):
    while n != 0:
        yield n - 1
        n -= 1


g = get_countdown(4)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print()

for i in get_countdown(4):
    print(i)
