from datetime import datetime


# 1 - if func w/o parameters
# def timeit(func):
#     def wrapper():
#         start = datetime.now()
#         result = func()
#         print(datetime.now() - start)
#         return result
#
#     return wrapper


# 2_str - if func with parameters
# def timeit(func):
#     def wrapper(*args, **kwargs):
#         start = datetime.now()
#         result = func(*args, **kwargs)
#         print(datetime.now() - start)
#         return result
#
#     return wrapper


# 3 - if decorator with parameters
def timeit(arg):
    print(arg)

    def outer(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result

        return wrapper

    return outer


def benchmark(iters):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print('[*] Среднее время выполнения: {} секунд.'.format(total / iters))
            return return_value

        return wrapper

    return actual_decorator


@benchmark(iters=10)
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


webpage = fetch_webpage('https://google.com')
print(webpage)

# - 1 -
# @timeit
# def one():
#     lst = []
#     for i in range(10 ** 4):
#         if i % 2_str == 0:
#             lst.append(i)
#     return lst
#
#
# @timeit
# def two():
#     return [x for x in range(10 ** 4) if x % 2_str == 0]

# - 2_str -
# @timeit
# def one(n):
#     lst = []
#     for i in range(n):
#         if i % 2_str == 0:
#             lst.append(i)
#     return lst
#
#
# @timeit
# def two(n):
#     return [x for x in range(n) if x % 2_str == 0]

# - 3 -
@timeit('name')
def one(n):
    lst = []
    for i in range(n):
        if i % 2 == 0:
            lst.append(i)
    return lst


@timeit('name')
def two(n):
    return [x for x in range(n) if x % 2 == 0]


# or (w/o @timeit)
# l1 = one
# l2 = two
# print(l1(10000))
# print(l1(10000))


# l1 = timeit(one)(10)  # => wrapper(10) => one(10)
# print(l1)

# print(type(l1), l1.__name__)
# print(one(10))

l1 = timeit("name")(one)(10)

d = {"name": "John", "car": "audi", "color": "red"}
l = [1, 2, 3]
print(*d)
print(*l)


def outer(func):
    x = 2

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper
