"""
The Crockford Invocation
The Coupon Code
"""
import datetime


def add(a):
    return lambda b: a + b


def subtract(a):
    return lambda b: a - b


def multiply(a):
    return lambda b: a * b


def apply(op):
    return op


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    current_date_parse = datetime.datetime.strptime(current_date, '%B %d, %Y')
    expiration_date_parse = datetime.datetime.strptime(expiration_date, '%B %d, %Y')
    if entered_code is correct_code:
        return current_date_parse <= expiration_date_parse
    else:
        return False
