"""
https://www.codewars.com/kata/5d50e3914861a500121e1958

https://www.codewars.com/kata/52b305bec65ea40fe90007a7
"""


def grabscrab(verb, possible_words):
    return [word for word in possible_words if sorted(word) == sorted(verb)]


print(grabscrab("trisf", ["first"]) == ["first"], "Should have found 'first'")
print(grabscrab("oob", ["bob", "baobab"]) == [], "Should not have found anything")
print(grabscrab("ainstuomn", ["mountains", "hills", "mesa"]) == ["mountains"], "Should have found 'mountains'")
print(grabscrab("oolp", ["donkey", "pool", "horse", "loop"]) == ["pool", "loop"], "Should have found 'pool' and 'loop'")
print(grabscrab("ortsp", ["sport", "parrot", "ports", "matey"]) == ["sport", "ports"],
      "Should have found 'sport' and 'ports'")
print(grabscrab("ourf", ["one", "two", "three"]) == [], "Should not have found anything")
