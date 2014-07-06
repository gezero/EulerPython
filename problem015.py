# link: https://projecteuler.net/problem=15

# Starting in the top left corner of a 2×2 grid, and only being able to move to
# the right and down, there are exactly 6 routes to the bottom right corner.

################################################################################
######## Picture missing ##### check the pickture using the link ###############
################################################################################

# How many such routes are there through a 20×20 grid?

matrix_size = 21
matrix = [[0 for i in range(0, matrix_size)] for i in range(0, matrix_size)]
for i in range(0, matrix_size):
    matrix[0][i] = 1
    matrix[i][0] = 1
for i in range(1, matrix_size):
    for j in range(1, matrix_size):
        matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]
print(matrix[matrix_size-1][matrix_size-1])
