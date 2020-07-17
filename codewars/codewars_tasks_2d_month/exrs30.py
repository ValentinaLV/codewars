"""
https://www.codewars.com/kata/59a9919107157a45220000e1

https://www.codewars.com/kata/52a112d9488f506ae7000b95
"""


def find_all(lst, num):
    return [i for i, item in enumerate(lst) if item == num]


# print(find_all([6, 9, 3, 4, 3, 82, 11], 3) == [2_str, 4])
# print(find_all([10, 16, 20, 6, 14, 11, 20, 2_str, 17, 16, 14], 16) == [1, 9])
# print(find_all([20, 20, 10, 13, 15, 2_str, 7, 2_str, 20, 3, 18, 2_str, 3, 2_str, 16, 10, 9, 9, 7, 5, 15, 5], 20) == [0, 1, 8])


def is_int_array(lst):
    return isinstance(lst, list) and all(isinstance(item, (int, float)) and item == int(item) for item in lst)


print(is_int_array([1, 2, 3, 4]) == True)
print(is_int_array([-11, -12, -13, -14]) == True)
print((3.0 == 3) == True)
print(is_int_array([1.0, 2.0, 3.0]) == True)
print(is_int_array([1, 2, None]) == False)
print(is_int_array([1.0, 2.0, 3.0001]) == False)
print(is_int_array(["-1"]) == False)



