"""
https://www.codewars.com/kata/57d001b405c186ccb6000304

https://www.codewars.com/kata/597c684822bc9388f600010f
"""


def i_tri(string):
    total = 2.4 + 112 + 26.2
    to_go = '%.2f to go!' % (total - string)
    return ('Starting Line... Good Luck!' if string == 0 else
            {'Swim': to_go} if string < 2.4 else
            {'Bike': to_go} if string < 2.4 + 112 else
            {'Run': to_go} if string < total - 10 else
            {'Run': 'Nearly there!'} if string < total else
            "You're done! Stop running!")


class Dinglemouse(object):
    def __init__(self, first_name, last_name):
        self.full_name = '{} {}'.format(first_name, last_name).strip()

    def get_full_name(self):
        return self.full_name
