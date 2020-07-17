def task1():
    """
     Возьмем строку "I love Python". Напишите код, который выведет символы до буквы "t".
    :return:
    """
    txt = "I love Python"
    i = 0
    while txt[i] != "t":
        print(txt[i], end="")
        i += 1


# task1()


def task2():
    """
    Возьмем строку "I love Python". Напишите код, который выведет эту строку без пробелов.
    :return:
    """
    s = "I love Python"
    for i in s:
        if i == ' ':
            continue
        else:
            print(i, end='')


# task2()


def task3(lst):
    """
    Создайте новый лист с помощью конвертации списка числовых строк в список чисел.
    :return:
    """
    # return [int(s) for s in lst]
    return list(map(lambda x: int(x), lst))


# print(task3(["23", "44"]))


def fib_seq(n):
    lst = [0, 1]
    num1, num2 = 1, 1
    for i in range(n - 1):
        num1, num2 = num2, num1 + num2
        lst.append(num1)
    return lst


print(fib_seq(10))


def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


print(fib(10))


def fact(n):
    value = 1
    while n >= 1:
        value *= n
        n -= 1
    return value


print(fact(5))


def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


print(bubble_sort([3, 2, 1]))


def get_sum(lst):
    # return sum([n for n in lst if lst.index(n) % 2_str]) * \
    #        sum([n for n in lst if lst.index(n) % 2_str == 0])
    return sum(lst[1::2]) * sum(lst[::2])


def count_letter(s):
    return s.count(char)
