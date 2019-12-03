"""
Well of Ideas - Harder Version
Convert the score
"""
import itertools


def well(arr):
    merged = [el.lower() for el in list(itertools.chain(*arr)) if isinstance(el, str)]
    if merged.count('good') == 1 or merged.count('good') == 2:
        return 'Publish!'
    elif merged.count('good') > 2:
        return 'I smell a series!'
    else:
        return 'Fail!'


print(well([['bad', 'bAd', 'bad'], ['bad', 'bAd', 'bad'], ['bad', 'bAd', 'bad']]) == 'Fail!')
print(well([['gOOd', 'bad', 'BAD', 'bad', 'bad'], ['bad', 'bAd', 'bad'], ['GOOD', 'bad', 'bad', 'bAd']]) == 'Publish!')
print(well([['gOOd', 'bAd', 'BAD', 'bad', 'bad', 'GOOD'], ['bad'], ['gOOd', 'BAD']]) == 'I smell a series!')


def scoreboard(string):
    goals = {
        'nil': 0, 'one': 1, 'two': 2, 'three': 3,
        'four': 4, 'five': 5, 'six': 6, 'seven': 7,
        'eight': 8, 'nine': 9
    }
    return [goals[num] for num in string.split() if num in goals]


print(scoreboard("The score is four nil") == [4, 0])
print(scoreboard("new score: two three") == [2, 3])
print(scoreboard("two two") == [2, 2])
print(scoreboard("Arsenal just conceded another goal, two nil") == [2, 0])
