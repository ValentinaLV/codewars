"""
https://www.codewars.com/kata/5809b62808ad92e31b000031
https://stackoverflow.com/questions/13055884/parsing-math-expression-in-python-and-solving-to-find-an-answer

https://www.codewars.com/kata/5a959662373c2e761d000183
"""


def calculate(string: str):
    return str(sum(int(num) for num in string.replace("minus", "plus-").split("plus")))


print(calculate('1plus2plus3plus4') == '10')
print(calculate('1minus2minus3minus4') == '-8')
print(calculate('1plus2plus3minus4') == '2')


def ticker(text, width, tick):
    string = ' ' * width + text
    tick %= len(string)
    return (string[tick:] + string[:tick])[:width]


print(ticker('Beautiful is better than ugly.', 10, 5) == '     Beaut')
print(ticker('Beautiful is better than ugly.', 10, 30) == 'than ugly.')
