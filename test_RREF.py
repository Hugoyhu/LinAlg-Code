# for testing RREF.py

import matrix


def test(data, soln):
    """
    Test RREF function with data input and soln output
    """
    m = matrix.Matrix()
    m.list_dataloader(data)
    m.solve_RREF()
    print(data == soln)


data1 = [
    [1, 2, 1, 3],
    [2, 3, 0, 7],
    [1, 1, 1, 2],
]

test1 = [
    [1, 0, 0, 2],
    [0, 1, 0, 1],
    [0, 0, 1, -1],
]

data2 = [
    [1, 0, 9, 10],
    [0, 1, -3, -3],
    [0, 0, 0, 0],
]

test2 = [
    [1, 0, 9, 10],
    [0, 1, -3, -3],
    [0, 0, 0, 0],
]

data3 = [
    [1, 2, 1, 0],
    [1, 3, -1, 0],
    [0, 1, 2, 0],
]

test3 = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
]

data4 = [
    [1, 2, 3, 4],
    [1, 3, 0, 1],
]

test4 = [
    [1, 0, 9, 10],
    [0, 1, -3, -3],
]

data5 = [
    [1, 2, 3, 1, 8],
    [1, 3, 0, 1, 7],
    [1, 0, 2, 1, 3],
]

test5 = [
    [1, 0, 0, 1, 1],
    [0, 1, 0, 0, 2],
    [0, 0, 1, 0, 1],
]


test(data1, test1)
test(data2, test2)
test(data3, test3)
test(data4, test4)
test(data5, test5)
