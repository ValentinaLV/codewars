"""
https://stackoverflow.com/questions/32238196/how-does-the-key-argument-in-pythons-sorted-function-work

https://runestone.academy/runestone/books/published/fopp/Sorting/Optionalkeyparameter.html
"""
# sorted
# ----------1----------
votes = {'Charlie': 20, 'Able': 10, 'Baker': 20, 'Dog': 15}
# list of tuples, each tuple having two items indexed 0 and 1

# [('Able', 10), ('Dog', 15), ('Charlie', 20), ('Baker', 20)]
print(sorted(votes.items(), key=lambda x: x[1]))

# [('Able', 10), ('Baker', 20), ('Charlie', 20), ('Dog', 15)]
print(sorted(votes.items(), key=lambda x: x[0]))

# ----------2----------
lst = ['aaaaaa', 'bb', 'ccc', 'd']
lst_len = sorted(lst, key=len)
print(lst_len)  # ['d', 'bb', 'ccc', 'aaaaaa']

# sort
data = ['abc', 'def', 'ghi', 'jkl']
data_s = data.sort(key=lambda s: s[::-1])
print(data_s)  # None
print(data)


def absolute(x):
    if x >= 0:
        return x
    else:
        return -x


lst2 = [1, 7, 4, -2, 3]
lst_abs = sorted(lst2, key=lambda x: x if x >= 0 else -x)
lst_abs2 = sorted(lst2, reverse=True, key=absolute)
print(lst_abs)
print(lst_abs2)
print(absolute(3))
print(absolute(-119))

# -----------------
# You will be sorting the following list by each element’s second letter, a to z.
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
sorted_by_second_let = sorted(ex_lst, key=lambda c: c[1])
print(sorted_by_second_let)

# Below, we have provided a list of strings called nums.
# Write a function called last_char that takes a string
# as input, and returns only its last character.
# Use this function to sort the list nums by the last digit of each number,
# from highest to lowest, and save this as a new list called nums_sorted.
nums = ['1450', '33', '871', '19', '14378', '32', '1005', '44', '8907', '16']
nums_sorted = sorted(nums, reverse=True, key=lambda x: x[len(x) - 1])
print(nums_sorted)