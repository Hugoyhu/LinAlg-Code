# Testing use only to validate matrix.py!

from matrix import Matrix
import tabulate

data1 = [
    [1, 1, 1, 2],
    [1, 2, 3, 7],
    [2, 3, 4, 13],
]

data2 = [
    [1, 1, 1, 2],
    [1, 2, 3, 7],
    [2, 3, 4, 13],
    [2, 3, 4, 13],
]

mat1 = Matrix()
mat1.list_dataloader(data1)

mat2 = Matrix()
mat2.list_dataloader(data2)

print(mat1)
print(mat2)

# print(mat1.matrix_product_entry(mat2, 0, 0))

outmat = mat1.multiply(mat2)

print(outmat)


def test_transpose():
    # 2x3 matrix -> transpose should be 3x2
    data = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    m = Matrix()
    m.list_dataloader(data)

    t = m.transpose()
    expected = [
        [1.0, 4.0],
        [2.0, 5.0],
        [3.0, 6.0],
    ]
    # transpose returns a numpy array; compare as lists
    print(t.tolist() == expected)


def test_field_multiply():
    # (2x3) * (3x2) -> (2x2), then modulo 2
    a_data = [
        [1, 1, 0],
        [0, 1, 1],
    ]
    b_data = [
        [1, 0],
        [1, 1],
        [0, 1],
    ]

    a = Matrix()
    a.list_dataloader(a_data)
    b = Matrix()
    b.list_dataloader(b_data)

    gf2_product = a.field_multiply(b)

    # Compute expected over Z_2 manually:
    # a * b = [[(1*1+1*1+0*0), (1*0+1*1+0*1)],
    #          [(0*1+1*1+1*0), (0*0+1*1+1*1)]] % 2
    expected = [
        [0.0, 1.0],
        [1.0, 0.0],
    ]

    print(gf2_product.tolist() == expected)


def test_multiply():
    data1 = [
        [1, 1, 1, 2],
        [1, 2, 3, 7],
        [2, 3, 4, 13],
    ]

    data2 = [
        [1, 1, 1, 2],
        [1, 2, 3, 7],
        [2, 3, 4, 13],
        [2, 3, 4, 13],
    ]

    m1 = Matrix()
    m1.list_dataloader(data1)

    m2 = Matrix()
    m2.list_dataloader(data2)

    result = m1.multiply(m2)

    expected_data = [
        [8, 12, 16, 48],
        [23, 35, 47, 146],
        [39, 59, 79, 246],
    ]

    expected = Matrix()
    expected.list_dataloader(expected_data)

    print(result == expected)


test_transpose()
test_field_multiply()
test_multiply()

# mat2 = Matrix()
# mat2.csv_dataloader("matrix.txt")

# print(mat2)

# print(mat1.can_multiply_matrices(mat2))


# mat.interchange_rows(1, 2)
# print(mat)
# mat.scale_row(2, 2)
# print(mat)
# mat.add_linear_multiple(2, 0, 10)
# print(mat)
# mat.interchange_rows(2, 0)
# print(mat)
# mat.scale_row(1, -2)
# print(mat)
# mat.add_linear_multiple(0, 2, -1)
# print(mat)
# mat.add_linear_multiple(0, 0, 1)
# print(mat)
