"""
https://www.codewars.com/kata/52829c5fe08baf7edc00122b

https://www.codewars.com/kata/5832db03d5bafb7d96000107

https://www.codewars.com/kata/56414fdc6488ee99db00002c
"""


def number_of_occurrences(element, sample_lst):
    return sample_lst.count(element)


sample = [0, 1, 2, 2, 3]
print(number_of_occurrences(0, sample), 1)
print(number_of_occurrences(4, sample), 0)
print(number_of_occurrences(2, sample), 2)
print(number_of_occurrences(3, sample), 1)


def lottery(s):
    if not s.isalpha() and s:
        return ''.join(el for el in sorted(set(s), key=s.index) if el.isdigit())
    return "One more run!"
    # result = ''
    # for el in string:
    #     if el.isdigit() and el not in result:
    #         result += el
    # return result


print(lottery("wQ8Hy0y5m5oshQPeRCkG"), "805")
print(lottery("ffaQtaRFKeGIIBIcSJtg") == "One more run!")
print(lottery("555") == "5")


def absent_vowel(string):
    return ['aeiou'.index(i) for i in 'aeiou' if i not in string][0]


print(absent_vowel("John Doe hs seven red pples under his bsket"), 0)
print(absent_vowel("Bb Smith sent us six neatly arranged range bicycles"), 3)

#print(0 + "a")
print(list(range(3)))