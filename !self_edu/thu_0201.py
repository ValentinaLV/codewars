"""

"""


def odd_or_even(arr):
    return 'odd' if sum(arr) % 2 else 'even'


def namelist(names):
    if len(names) == 1:
        return names[0]['name']
    elif len(names) > 1:
        return ', '.join(n['name'] for n in names[:-1]) + \
               ' & ' + names[-1]['name']
    return ''


# print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]))
# print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}])
#       == 'Bart, Lisa, Maggie, Homer & Marge')
# print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]) == 'Bart & Lisa')
# print(namelist([{'name': 'Bart'}]) == 'Bart')


def solution(string, ending):
    # return string.endswith(ending)
    return string[(len(string) - len(ending)):] == ending


# print(solution('abcde', 'cde') == True)
# print(solution('abcde', 'abc') == False)
# print(solution('abcde', '') == True)


def is_square(n):
    # return (n ** 0.5).is_integer() if n >= 0 else False
    return (n ** 0.5) % 1 == 0 if n >= 0 else False
    # return n > -1 and math.sqrt(n) % 1 == 0

print(is_square(0) == True)
print(is_square(-1) == False)
print(is_square(25) == True)
print(is_square(26) == False)
