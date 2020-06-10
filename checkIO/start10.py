"""

"""


def checkio(first, second):
    inter = set(first.split(',')).intersection(
        set(second.split(','))
    )
    return ','.join(sorted(inter))


if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello"
    assert checkio("one,two,three", "four,five,six") == ""
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"

from collections import Counter

from string import ascii_lowercase
def checkio2(text: str) -> str:
    # d = {c: text.count(c) for c in sorted(text.lower())}
    # return sorted(d.items(), key=lambda x: x[1], reverse=True)[0][0]
    text = ''.join(c for c in text.lower() if c in ascii_lowercase)
    return Counter(sorted(text.lower())).most_common()[0][0]


if __name__ == '__main__':
    print("Example:")
    print(checkio2("AAaooo!!!!"))

    assert checkio2("Hello World!") == "l"
    assert checkio2("How do you do?") == "o"
    assert checkio2("One") == "e"
    assert checkio2("Oops!") == "o"
    assert checkio2("AAaooo!!!!") == "a"
    assert checkio2("abe") == "a"
    print("Start the long test")
    assert checkio2("a" * 9000 + "b" * 1000) == "a"
    print("The local tests are done.")

from string import ascii_lowercase


def check_pangram(text):
    '''
        is the given text is a pangram.
    '''
    lst = [c for c in text.lower() if c in ascii_lowercase]
    return len(set(lst)) == len(set(ascii_lowercase))


if __name__ == '__main__':
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
    print('If it is done - it is Done. Go Check is NOW!')


def from_camel_case(name):
    # return re.sub(r'([A-Z])', r'_\1', name)[1:].lower()
    new = ''
    for c in name[1:]:
        if c.isupper():
            new += f'_{c.lower()}'
        else:
            new += c
    return f'{name[0].lower()}{new}'


if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("MyFunctionName"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")


def to_camel_case(name):
    new_str = name.replace('_', ' ')
    return ''.join(c for c in new_str.title() if not c.isspace())
    #return "".join(name.title().split("_"))


if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('my_function_name'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
