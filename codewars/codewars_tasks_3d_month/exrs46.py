"""
https://www.codewars.com/kata/5a4ea304b3bfa89a9900008e

https://www.codewars.com/kata/5e297e9f63f1db003317cbac
"""


def max_number(num):
    #return int(''.join(sorted(str(num), reverse=True)))
    lst = sorted(str(n) for n in str(num))[::-1]
    return int(''.join(lst))


print(max_number(213) == 321)
print(max_number(7389) == 9873)
print(max_number(63792) == 97632)
print(max_number(566797) == 977665)
print(max_number(1000000) == 1000000)


def paint_tiles(costs):
    t = [0] * 4
    for cs in costs:
        t = [c + min(t[j] for j in range(4) if j != i) for i, c in enumerate(cs)]
    return min(t)













