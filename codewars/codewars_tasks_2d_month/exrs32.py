"""
https://www.codewars.com/kata/58880c6e79a0a3e459000004

https://www.codewars.com/kata/53ea07c9247bc3fcaa00084d
"""


def house_numbers_sum(lst):
    # s = []
    # for n in inp:
    #     if 5 <= len(inp) <= 50 and 0 <= n <= 10:
    #         if n == 0:
    #             break
    #         else:
    #             s.append(n)
    # return sum(s)
    # s = []
    # for n in inp:
    #     if 5 <= len(inp) <= 50 and 0 <= n <= 10:
    #         s.append(n)
    # return sum(s[:s.index(0)])
    total = 0
    for house_num in lst:
        if house_num == 0:
            return total
        else:
            total += house_num


print(house_numbers_sum([5, 1, 2, 3, 0, 1, 5, 0, 2]) == 11)
print(house_numbers_sum([4, 2, 1, 6, 0]) == 13)
print(house_numbers_sum([4, 1, 2, 3, 0, 10, 2]) == 10)
print(house_numbers_sum([0, 1, 2, 3, 4, 5]) == 0)
print(house_numbers_sum([5, 1, 2, 3, 0, 1, 5, 0, 2]))
print(house_numbers_sum([4, 2, 1, 6, 0]))
print(house_numbers_sum([4, 1, 2, 3, 0, 10, 2]))
print(house_numbers_sum([0, 1, 2, 3, 4, 5]))
