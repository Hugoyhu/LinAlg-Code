# RREF test cases
import matrix


def test(data, soln):
    """
    Test RREF function with data input and soln output
    """
    m = matrix.Matrix(data)
    m.solve_RREF()
    print("PASS" if data == soln else "FAIL")
    print("Result:", data)
    print("Expected:", soln)
    print("-" * 40)


data1 = [[2, 1, 5], [4, -6, -2]]
test1 = [[1, 0, 2], [0, 1, 1]]
test(data1, test1)

data2 = [[1, 0, 2], [0, 1, 3]]
test2 = [[1, 0, 2], [0, 1, 3]]
test(data2, test2)

data3 = [[1, 2, -1, 1], [2, 4, -2, 2]]
test3 = [[1, 2, -1, 1], [0, 0, 0, 0]]
test(data3, test3)

data4 = [[1, -2, 1], [2, -4, 5]]
test4 = [[1, -2, 1], [0, 0, 3]]
test(data4, test4)

data5 = [[0, 2, 3, 5], [2, 4, 6, 10], [1, 1, 1, 3]]
test5 = [[1, 0, -1, -1], [0, 1, 3 / 2, 5 / 2], [0, 0, 0, 0]]
test(data5, test5)

data6 = [[1, 1, 1, 6], [0, 2, 5, -4], [2, 5, -1, 27]]
test6 = [[1, 0, 0, 5], [0, 1, 0, 3], [0, 0, 1, -2]]
test(data6, test6)

data7 = [[1, 2, 3, 4], [0, 1, 4, 2], [0, 0, 0, 0]]
test7 = [[1, 0, -5, 0], [0, 1, 4, 2], [0, 0, 0, 0]]
test(data7, test7)

data8 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
test8 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
test(data8, test8)

data9 = [[1, 2, 3], [4, 5, 6]]
test9 = [[1, 0, -1], [0, 1, 2]]
test(data9, test9)

data10 = [[1, 2, 1, 3, 4], [2, 3, 0, 7, 1], [1, 1, 1, 2, 0], [0, 1, 2, 1, 5]]
test10 = [[1, 0, 0, 2, 1], [0, 1, 0, 1, 0], [0, 0, 1, -1, 1], [0, 0, 0, 0, 1]]
test(data10, test10)
