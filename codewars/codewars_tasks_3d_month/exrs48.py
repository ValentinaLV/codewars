"""
https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed

https://www.codewars.com/kata/525f50e3b73515a6db000b83
"""
from numpy import diff


def jumping_number(number):
    return 'Jumping!!' if set(abs(diff([int(n) for n in str(number)]))) == {1} or len(str(number)) == 1 else 'Not!!'


print(jumping_number(9) == "Jumping!!")
print(jumping_number(23) == "Jumping!!")
print(jumping_number(79) == "Not!!")
print(jumping_number(98) == "Jumping!!")


def create_phone_number(num):
    lst = [str(el) for el in num]
    return f'({"".join(lst[0:3])}) {"".join(lst[3:6])}-{"".join(lst[6:])}'
    # return "({}{}{}) {}{}{}-{}{}{}{}".format(*num)


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890")
print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "(111) 111-1111")
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "(123) 456-7890")
