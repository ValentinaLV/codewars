"""
https://stackoverflow.com/questions/32238196/how-does-the-key-argument-in-pythons-sorted-function-work
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
print(lst_len) # ['d', 'bb', 'ccc', 'aaaaaa']


# sort
data = ['abc', 'def', 'ghi', 'jkl']
data_s = data.sort(key=lambda s: s[::-1])
print(data_s) # None
print(data)