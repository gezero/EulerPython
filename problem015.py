matrix_size =20
matrix = [[0 for i in range(0,matrix_size)] for i in range(0,matrix_size)]
for i in range(0,matrix_size):
	matrix[0][i]=1
	matrix[i][0]=1
for i in range(1,matrix_size):
	for j in range(1,matrix_size):
		matrix[i][j]=matrix[i][j-1]+matrix[i-1][j]
print(matrix)
print(matrix[matrix_size-1][matrix_size-1])