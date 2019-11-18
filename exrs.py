'''
https://www.codewars.com/kata/54ff3102c1bad923760001f3
'''

def get_count(inputStr):
    '''
    Return the number (count) of vowels in the given string.
    We will consider a, e, i, o, and u as vowels for this Kata.
    The input string will only consist of lower case letters and/or spaces.
    :param input_str:
    :return:
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']
    return sum(inputStr.count(vowel) for vowel in vowels)


'''
https://www.codewars.com/kata/56dbe0e313c2f63be4000b25
'''
def vert_mirror(strng):
    return '\n'.join(s[::-1] for s in strng.split('\n'))


def hor_mirror(strng):
    return '\n'.join(reversed(strng.split('\n')))


def oper(fct, s):
    return fct(s)
