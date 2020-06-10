"""
https://www.codewars.com/kata/5a4d303f880385399b000001

https://www.codewars.com/kata/51e0007c1f9378fa810002a9
"""
from math import factorial


def strong_num(number):
    return "STRONG!!!!" if sum(factorial(int(num)) for num in str(number)) == number else "Not Strong !!"


print(strong_num(1) == "STRONG!!!!")
print(strong_num(2) == "STRONG!!!!")
print(strong_num(145) == "STRONG!!!!")
print(strong_num(7) == "Not Strong !!")
print(strong_num(93) == "Not Strong !!")
print(strong_num(185) == "Not Strong !!")


def parse(data):
    value = 0
    result_lst = []
    for char in data:
        if char == "i": value += 1
        elif char == "d": value -= 1
        elif char == "s": value *= value
        elif char == "o": result_lst.append(value)
    return result_lst


print(parse("ooo") == [0,0,0])
print(parse("ioioio") == [1,2,3])
print(parse("idoiido") == [0,1])
print(parse("isoisoiso") == [1,4,25])
print(parse("codewars") == [0])
