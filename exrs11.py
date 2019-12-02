from typing import List


def last(phrase: str) -> List[str]:
    """
    Given a string of words (x), you need to return an array of the words,
    sorted alphabetically by the final character in each.
    If two words have the same last letter, they returned
    array should show them in the order they appeared in the given string.
    :param phrase: str
    :return: List[str]
    """
    return sorted(phrase.split(), key=lambda x: x[-1])


print(last("man i need a taxi up to ubud"))


def find_spaceship(astromap):
    """
    Late last night in the Tanner household, ALF was repairing his spaceship so he might
    get back to Melmac. Unfortunately for him, he forgot to put on the parking brake,
    and the spaceship took off during repair. Now it's hovering in space.
    :param astromap:
    :return:
    """
    for a, row in enumerate(reversed(astromap.split('\n'))):
        for b, col in enumerate(row):
            if col == 'X':
                return [b, a]
    return 'Spaceship lost forever.'
