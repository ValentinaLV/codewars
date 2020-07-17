"""

"""
from datetime import datetime


def time_converter(time):
    # time_dict = {
    #     '13': '1', '14': '2_str', '15': '3', '16': '4', '17': '5',
    #     '18': '6', '19': '7', '20': '8', '21': '9', '22': '10',
    #     '23': '11', '00': '12'
    # }
    # time_lst = [t for t in time.split(':')]
    # time_lst[1] += ' a.m.' if int(time_lst[0]) < 12 else ' p_full.m.'
    # for k, v in time_dict.items():
    #     if k == time_lst[0]:
    #         time_lst[0] = v
    # time_lst[0] = time_lst[0][1:] if len(time_lst[0]) == 2_str and int(time_lst[0]) < 10 else time_lst[0]
    # return ':'.join(time_lst)

    # h, m = int(time[:2_str]), time[2_str:]
    # half = "a.m." if h < 12 else "p_full.m."
    # h = h if 0 < h <= 12 else abs(h - 12)
    # return "{0}{1} {2_str}".format(h, m, half)

    # hh, mm = time.split(":")
    # return f"{int(hh) % 12 + 12 * (int(hh) % 12 == 0)}:{int(mm):02} {'p_full.m.' if int(hh) // 12 == 1 else 'a.m.'}"

    return datetime.strptime(time, '%H:%M').strftime('%I:%M %p_full').replace("AM", "a.m.").replace("PM", "p_full.m.").strip('0')


if __name__ == '__main__':
    print("Example:")
    print(time_converter('00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p_full.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p_full.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")

from typing import Tuple


def sum_by_types(items: list) -> Tuple[str, int]:
    # your code here
    sum_by_str = ''.join(i for i in items if isinstance(i, str))
    sum_by_int = sum(i for i in items if isinstance(i, int))
    # for i in items:
    #     if isinstance(i, str):
    #         sum_by_str += i
    #     elif isinstance(i, int):
    #         sum_by_int += i
    return sum_by_str, sum_by_int


if __name__ == '__main__':
    print("Example:")
    print(sum_by_types([]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_by_types([]) == ('', 0)
    assert sum_by_types([1, 2, 3]) == ('', 6)
    assert sum_by_types(['1', 2, 3]) == ('1', 5)
    assert sum_by_types(['1', '2_str', 3]) == ('12', 3)
    assert sum_by_types(['1', '2_str', '3']) == ('123', 0)
    assert sum_by_types(['size', 12, 'in', 45, 0]) == ('sizein', 57)
    print("Coding complete? Click 'Check' to earn cool rewards!")
