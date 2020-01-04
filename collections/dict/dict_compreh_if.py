dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

dict1_cond1 = {k: v for (k, v) in dict1.items() if v > 2}
print(dict1_cond1)

# Multiple If Conditions
dict1_cond2 = {k: v for (k, v) in dict1.items() if v > 2 and v % 2 == 0}
print(dict1_cond2)

dict1_cond3 = {k: v for (k, v) in dict1.items() if v > 2 and v % 2 == 0 and v % 3 == 0}
print(dict1_cond3)

# If-Else Conditions
dict1_cond4 = {k: ('even' if v % 2 == 0 else 'odd') for (k, v) in dict1.items()}
print(dict1_cond4)