"""
https://www.codewars.com/kata/565b112d09c1adfdd500019c

https://www.codewars.com/kata/562c3b54746f50d28d000027
"""


def nth_char(words):
    # result_str = ""
    # for i, word in enumerate(words):
    #     result_str += word[i]
    # return result_str
    return ''.join(word[i] for i, word in enumerate(words))


print(nth_char(['yoda', 'best', 'has']) == 'yes')
print(nth_char([]) == '')
print(nth_char(['X-ray']) == 'X')
print(nth_char(['No', 'No']) == 'No')
print(nth_char(['Chad', 'Morocco', 'India', 'Algeria', 'Botswana', 'Bahamas', 'Ecuador', 'Micronesia']) == 'Codewars')

print(nth_char(['yoda', 'best', 'has']))


def decode(string):
    result_lst = []
    index = 0
    while index < len(string):
        if string[index] == '\\':
            index += 1
            n = ''
            while string[index].isdigit():
                n += string[index]
                index += 1
            result_lst.append(string[index:index + int(n)])
            index += int(n)
        else:
            result_lst.append(string[index])
            index += 1
    return result_lst


print(decode(''), [])
print(decode('abc') == ['a', 'b', 'c'])
print(decode("\\1abc") == ['a', 'b', 'c'])
print(decode("\\1a\\1bc") == ['a', 'b', 'c'])
print(decode("\\3a\\1bc") == ['a\\1', 'b', 'c'])
print(decode("\\10a\\1bc") == ['a\\1bc'])
