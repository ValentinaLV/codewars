"""
https://www.codewars.com/kata/5a53a17bfd56cb9c14000003

https://www.codewars.com/kata/5583d268479559400d000064
"""


def disarium_number(number):
    """
    Since , 81 + 92 = 89 , thus output is "Disarium !!"
    51 + 62 + 43 = 105 != 564 , thus output is "Not !!"
    :param number:
    :return:
    """
    return "Disarium !!" if sum(int(n) ** (i+1) for i, n in enumerate(str(number))) == number else "Not !!"


print(disarium_number(89) == "Disarium !!")
print(disarium_number(518) == "Disarium !!")
print(disarium_number(1024) == "Not !!")
print([int(n) ** (i+1) for i, n in enumerate(str(1024))])


def binary_to_string(binary):
    return "".join(chr(int(binary[i:i + 8], 2)) for i in range(0, len(binary), 8))
