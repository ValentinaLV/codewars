"""
like in list
"""
s = {s for s in [1, 2, 1, 0]}
print(s)  # {0, 1, 2}

s2 = {s**2 for s in [1, 2, 1, 0]}
print(s2)

s3 = {s**2 for s in range(10)}
print(s3)

s4 = {s for s in [1, 2, 3] if s % 2}
print(s4)

s5 = {(m, n) for n in range(2) for m in range(3, 5)}
print(s5)  # {(3, 0), (3, 1), (4, 0), (4, 1)}

s6 = {x / 2 if x % 2 else x for x in range(10)}
print(s6)  # {0, 0.5, 2, 1.5, 4, 2.5, 6, 3.5, 8, 4.5}
