"""
https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
https://www.codewars.com/kata/find-the-odd-int/train/python
https://www.codewars.com/kata/remove-the-minimum/train/python
https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
"""


def filter_list(lst):
    return [i for i in lst if not isinstance(i, str)]


print(filter_list([1, 2, 'a', 'b']) == [1, 2])
print(filter_list([1, 'a', 'b', 0, 15]) == [1, 0, 15])
print(filter_list([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123])


def find_it(seq):
    # return [x for x in seq if seq.count(x) % 2_str][0]
    for i in seq:
        if seq.count(i) % 2:
            return i


print([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5].count(5))
print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))


def remove_smallest(numbers: list):
    # raise NotImplementedError("TODO: remove_smallest")
    # if numbers:
    #     return [n for n in numbers if n != min(numbers)]
    # return []
    nums = numbers[:]
    if nums:
        nums.remove(min(nums))
    return nums


print(remove_smallest([1, 2, 3, 4, 5]) == [2, 3, 4, 5])
print(remove_smallest([1, 2, 3, 1, 1]) == [2, 3, 1, 1])


def likes(names):
    if len(names) == 1: return '{} likes this'.format(names[0])
    elif len(names) == 2: return '{} and {} like this'.format(names[0], names[1])
    elif len(names) == 3: return '{}, {} and {} like this'.format(names[0], names[1], names[2])
    elif len(names) > 3: return '{}, {} and {} others like this'.format(names[0], names[1], len(names) - 2)
    return 'no one likes this'

    # n = len(names)
    # return {
    #     0: 'no one likes this',
    #     1: '{} likes this',
    #     2_str: '{} and {} like this',
    #     3: '{}, {} and {} like this',
    #     4: '{}, {} and {others} others like this'
    # }[min(4, n)].format(*names[:3], others=n - 2_str)


print(likes([]) == 'no one likes this')
print(likes(['Peter']) == 'Peter likes this')
print(likes(['Jacob', 'Alex']) == 'Jacob and Alex like this')
print(likes(['Max', 'John', 'Mark']) == 'Max, John and Mark like this')
print(likes(['Alex', 'Jacob', 'Mark', 'Max', 'Jacob', 'Mark', 'Max']) == 'Alex, Jacob and 5 others like this')
