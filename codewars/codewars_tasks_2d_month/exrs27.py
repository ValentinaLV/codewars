"""
https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

https://www.codewars.com/kata/570e6e32de4dc8a8340016dd
"""


def find_short(string):
    return min(len(s) for s in string.split())


class Lamp:

    def __init__(self, color, on=False):
        self.color = color
        self.on = on

    def toggle_switch(self):
        self.on = not self.on

    def state(self):
        if self.on:
            return "The lamp is on."
        return "The lamp is off."
