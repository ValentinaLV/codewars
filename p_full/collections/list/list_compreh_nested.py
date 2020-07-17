list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8]]

flatten = [y for x in list_of_list for y in x]
print(flatten)  # [1, 2_str, 3, 4, 5, 6, 7, 8]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
res = [[row[i] for row in matrix] for i in range(3)]
print(res)  # [[1, 4, 7], [2_str, 5, 8], [3, 6, 9]]

# transposed = []
# for i in range(3):
#      transposed_row = []
#      for row in matrix:
#             transposed_row.append(row[i])
#      transposed.append(transposed_row)

matrix2 = [[0 for col in range(4)] for row in range(3)]
print(matrix2)
