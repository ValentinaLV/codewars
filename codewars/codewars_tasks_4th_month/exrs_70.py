"""
https://www.codewars.com/kata/5a87449ab1710171300000fd

https://www.codewars.com/kata/5a58d889880385c2f40000aa
"""


def tidy_number(num):
    return list(str(num)) == sorted(str(num))


print(tidy_number(12), True)
print(tidy_number(102), False)
print(tidy_number(9672), False)
print(tidy_number(2789), True)


def automorphic(num):
    # return "Automorphic" if str(num)[-1] == str(num * num)[-1] else "Not!!"
    return "Automorphic" if str(num * num).endswith(str(num)) else "Not!!"


print(automorphic(1), "Automorphic")
print(automorphic(3), "Not!!")
print(automorphic(6), "Automorphic")
print(automorphic(9), "Not!!")
print(automorphic(25), "Automorphic")
print(automorphic(53), "Not!!")
print(automorphic(76), "Automorphic")
print(automorphic(95), "Not!!")
print(automorphic(625), "Automorphic")
print(automorphic(225), "Not!!")
