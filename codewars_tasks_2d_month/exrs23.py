"""
https://www.codewars.com/kata/57ed7214f670e99f7a000c73

https://www.codewars.com/kata/54dc6f5a224c26032800005c
"""


def ski_jump(mountain):
    height = len(mountain)
    speed = height * 1.5
    length = (height * speed * 9) / 10
    return (f'{length:.2f} metres: He\'s crap!' if length < 10 else
            f'{length:.2f} metres: He\'s ok!' if length < 25 else
            f'{length:.2f} metres: He\'s flying!' if length < 50 else
            f'{length} metres: Gold!!')


def ski_jump(mountain):
    height = len(mountain)
    speed = height * 1.5
    length = (height * speed * 9) / 10
    if length < 10: return f'{length:.2f} metres: He\'s crap!'
    if length < 25: return f'{length:.2f} metres: He\'s ok!'
    if length < 50: return f'{length:.2f} metres: He\'s flying!'
    return f'{length:.2f} metres: Gold!!'


print(ski_jump(["*"]))
print(ski_jump(["*", "**", "***"]))
print(ski_jump(["*", "**", "***", "****", "*****", "******"]))
print(ski_jump(["*"]) == "1.35 metres: He's crap!")
print(ski_jump(["*", "**", "***"]) == "12.15 metres: He's ok!")
print(ski_jump(["*", "**", "***", "****", "*****", "******"]) == "48.60 metres: He's flying!")


def stock_list(stock_list, categories):
    if not stock_list or not categories:
        return ""
    return " - ".join(
        "({} : {})".format(
            category,
            sum(int(item.split()[1]) for item in stock_list if item[0] == category))
        for category in categories)


b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
lst = ['A', 'B']
d = {}
b1 = [i.split() for i in b]
print(b1)

for k, v in b1:
    d[k] = int(v)

print(d)

suma = 0
for i in lst:
    for k, v in d.items():
        if i in k[0]:
            suma += v
print(suma)

print(stock_list(b, lst))
