"""
https://www.codewars.com/kata/5a55f04be6be383a50000187

https://www.codewars.com/kata/5a057ec846d843c81a0000ad
"""


def special_number(number):
    return "Special!!" if all(n in range(6) for n in [int(n) for n in str(number)]) else "NOT!!"
    #return "Special!!" if set([int(n) for n in str(number)]).issubset(range(6)) else "NOT!!"


print(special_number(23) == "Special!!")
print(special_number(79) == "NOT!!")
print(special_number(39) == "NOT!!")
print(special_number(55) == "Special!!")


def cycle(n):
    pass

# one = [1, 2, 3]
# two = [9, 8, 5, 3, 2, 1]
#
# all(x in two for x in one)