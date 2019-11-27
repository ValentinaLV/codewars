"""
The Crockford Invocation
"""


def add(a):
    return lambda b: a + b


def subtract(a):
    return lambda b: a - b


def multiply(a):
    return lambda b: a * b


def apply(op):
    return op
