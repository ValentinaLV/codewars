def solution(string: str, ending: str):
    return string.endswith(ending)


def solution2(string: str, ending: str):
    len_str_start = len(string) - len(ending)
    str_end = string[len_str_start:]
    return str_end == ending


print(solution2("hello", "mo"))


def fib(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    return fib(num - 2) + fib(num - 1)


def fib2(num):
    res_two_nums = 0
    iterator = 1
    frst_num = 0
    sec_num = 1
    while iterator < num:
        res_two_nums = frst_num + sec_num
        frst_num, sec_num = sec_num, res_two_nums
        iterator += 1
    return res_two_nums


# optimal fib
def fib3(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


print(fib(10))
print(fib2(10))
print(fib3(10))


def fib4(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a


def get_fib_seq(num):
    i = 2
    fib_arr = [0, 1]
    if num < len(fib_arr):
        return fib_arr
    while i <= num:
        fib_arr.append(fib3(i))
        i += 1
    return fib_arr


print(get_fib_seq(10))


# optimal prod fib
def product_fib(prod):
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b
    return [a, b, prod == a * b]


print(product_fib(4895) == [55, 89, True])
print(product_fib(5895) == [89, 144, False])
