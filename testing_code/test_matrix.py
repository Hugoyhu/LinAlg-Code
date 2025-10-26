# Testing use only to validate matrix.py!

from matpy import Matrix

data = [
    [1, 1, 1, 2],
    [1, 2, 3, 7],
    [2, 3, 4, 13],
]

mat = Matrix(data)
print(mat)
mat.interchange_rows(1, 2)
print(mat)
mat.scale_row(2, 2)
print(mat)
mat.add_linear_multiple(2, 0, 10)
print(mat)
mat.interchange_rows(2, 0)
print(mat)
mat.scale_row(1, -2)
print(mat)
mat.add_linear_multiple(0, 2, -1)
print(mat)
mat.add_linear_multiple(0, 0, 1)
print(mat)
