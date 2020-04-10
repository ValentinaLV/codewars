# reverse each element in list

lst = [1, 2, 3, 4, 5]

for i in range(0, len(lst) - 1, 2):
    lst[i], lst[i + 1] = lst[i + 1], lst[i]

print(lst)

# транспонувати матрицю
lst2 = [[1, 2, 3], [4, 5, 6]]
res = list(zip(*lst2))

print(res)

# без включень
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = []
for el in lst:
    for i in el:
        res.append(i)
print(res)

a = 'dffdfdfsfss'
lst = [(j, a.count(j)) for i, j in enumerate(a)]