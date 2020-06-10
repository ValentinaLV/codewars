"""
exercises from 20112019
"""


def remove_url_anchor(url: str) -> str:
    """
    Remove anchor from URL
    :param url: str
    :return: str
    """
    return url.split('#')[0]


def sort_gift_code(code: str) -> str:
    """
    Sort the Gift Code
    :param code: str
    :return: str
    """
    return ''.join(sorted(code))
