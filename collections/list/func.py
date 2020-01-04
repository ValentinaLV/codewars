"""
reversed()
sorted()
"""

lst = ['apple', 'lemon', 'blackcurrant', 'cherry', 'orange', 'kiwi', 'melon', 'mango', 'peanut']

print(reversed(lst))  # <list_reverseiterator object at 0x10435cf60>
print(lst)
# create new list
lst_reversed = list(reversed(lst))
print(lst_reversed)  # ['peanut', 'mango', 'melon', 'kiwi', 'orange', 'cherry', 'blackcurrant', 'lemon', 'apple']

print(sorted(lst))  # ['apple', 'blackcurrant', 'cherry', 'kiwi', 'lemon', 'mango', 'melon', 'orange', 'peanut']
print(sorted(lst, reverse=True))  # ['peanut', 'orange', 'melon', 'mango', 'lemon', 'kiwi', 'cherry', 'blackcurrant', 'apple']
