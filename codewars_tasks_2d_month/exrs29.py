"""
https://www.codewars.com/kata/54ba84be607a92aa900000f1


"""
import math


def is_isogram(string):
    # return len(string) == len(set(string.lower()))
    return True if len(string) == sum(string.lower().count(s) for s in string.lower()) else False


print(is_isogram("Dermatoglyphics") == True)
print(is_isogram("isogram") == True)
print(is_isogram("aba") == False)
print(is_isogram("moOse") == False)
print(is_isogram("isIsogram") == False)
print(is_isogram("") == True)
print(is_isogram("xptnyxyayxc") == False)


def solve(lst):
    lst_sort = sorted(lst)
    if lst_sort[0] + lst_sort[1] < lst_sort[2]:
        return lst_sort[0] + lst_sort[1]
    else:
        return math.floor((lst_sort[0] + lst_sort[1] + lst_sort[2]) / 2)


# @test_package.describe('Fixed Tests')
# def fixed_tests():
#     @test_package.it('Basic Test Cases')
#     def basic_tests():
#         test_package.assert_equals(solve([1,1,1]), 1)
#         test_package.assert_equals(solve([1,2,1]), 2)
#         test_package.assert_equals(solve([4,1,1]), 2)
#         test_package.assert_equals(solve([8,2,8]), 9)
#         test_package.assert_equals(solve([8,1,4]), 5)
#         test_package.assert_equals(solve([7,4,10]), 10)
#         test_package.assert_equals(solve([12,12,12]), 18)
#         test_package.assert_equals(solve([1,23,2]), 3)