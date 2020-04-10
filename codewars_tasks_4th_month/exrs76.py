"""
https://www.codewars.com/kata/514a024011ea4fb54200004b


"""


def domain_name(url):
    return url.split('//')[-1].split('www.')[-1].split('.')[0]


# print(domain_name("http://google.com"), "google")
# print(domain_name("http://google.co.jp"), "google")
# print(domain_name("www.xakep.ru"), "xakep")
# print(domain_name("https://youtube.com"), "youtube")


def string_expansion(string):
    # Good Luck!
    char, num = '', 1
    for i in string:
        if i.isdigit():
            num = int(i)
        else:
            char += i * num
    return char


print(string_expansion('3abc'), 'aaabbbccc')
print(string_expansion('3D2a5d2f'), 'DDDaadddddff')
print(string_expansion('0d0a0v0t0y'), '')
print(string_expansion('3d332f2a'), 'dddffaa')
print(string_expansion('abcde'), 'abcde')


def highest_rank(arr):
    # your code here
    # d = {k: arr.count(k) for k in arr}
    # return max(d, key=lambda key: d[key])
    return sorted(arr, key=lambda x: (arr.count(x), x))[-1]


print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]), 12)
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]), 10)
