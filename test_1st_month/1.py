# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

# ----1----
# Write a program to swap the elements above the main diagonal
# in the square matrix and #symmetrical elements below the main diagonal.


def swap_el_diagonal(matrix):
    for i in range(3):
        matrix[i][i], matrix[i][3 - i - 1] = matrix[i][3 - i - 1], matrix[i][i]


def display_swapped_el_matrix(matrix):
    swap_el_diagonal(matrix)
    for i in range(3):
        for j in range(3):
            print(matrix[i][j], end=' ')
        print()


matrix = [[0, 1, 2],
          [3, 4, 5],
          [6, 7, 8]]

display_swapped_el_matrix(matrix)
