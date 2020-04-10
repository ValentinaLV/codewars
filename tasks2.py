def tag_wrapper(func):
    def wrapper(*args, **kwargs):
        result = '<h1>' + func(*args, **kwargs) + '</h1>'
        return result

    return wrapper


@tag_wrapper
def get_str(s):
    return s

print(get_str('hello'))