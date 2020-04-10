"""
https://www.codewars.com/kata/567e8f7b4096f2b4b1000005



"""

eight_bit_number = lambda n: n in map(str, range(256))

print(eight_bit_number(256))


def eight_bit_number(num):
    return num in [str(num) for num in range(256)]


print(eight_bit_number(256))


def six_bit_number(num):
    return num in [str(n) for n in range(64)]


from string import ascii_lowercase, digits


def count_letters_and_digits(string):
    counter = 0
    for char in string:
        if char.lower() in ascii_lowercase or char in digits:
            counter += 1
    return counter
    #return sum([string.count(c) for c in string if c.lower() in ascii_lowercase or c in digits])
    #return isinstance(s, str) and sum(map(str.isalnum, s))




print(count_letters_and_digits('n!!ice!!123') == 7)
print(count_letters_and_digits('de?=?=tttes!!t'), 8)
print(count_letters_and_digits('') == 0)
print(count_letters_and_digits('!@#$%^&`~.') == 0)
print(count_letters_and_digits('u_n_d_e_r__S_C_O_R_E') == 10)
