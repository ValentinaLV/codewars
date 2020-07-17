from datetime import datetime


def tag_wrapper(func):
    def wrapper(*args, **kwargs):
        return f'<h1>{func(*args, **kwargs)}</h1>'

    return wrapper


# func with parameters
def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result

    return wrapper


# func w/o parameters
def timeit2(func):
    def wrapper():
        start = datetime.now()
        result = func()
        print(datetime.now() - start)
        return result

    return wrapper

import time
# decorator with parameters
def banchmark(iters):
    def outer(func):
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                result = func(*args, **kwargs)
                total += round(time.time() - start, 10)
            print(f'Actual time for {iters} iterations is {total}')
            return result

        return wrapper

    return outer


@timeit
@tag_wrapper
@banchmark(iters=150)
def get_tagged_str(string):
    return string


print(get_tagged_str('hello'))


@timeit2
def get_str():
    return 'Why'


print(get_str())
