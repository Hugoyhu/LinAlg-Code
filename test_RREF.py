# for testing RREF.py

import matrix


# def test(data, soln):
#     """
#     Test RREF function with data input and soln output
#     """
#     m = matrix.Matrix()
#     m.list_dataloader(data)
#     m.solve_RREF()
#     print(data == soln)


def test(data, soln):
    """
    Test RREF function with data input and soln output
    """
    m = matrix.Matrix()
    m.list_dataloader(data)
    m.solve_switch_RREF()
    result = m.data == soln
    print(result)
    return result


# Test Case 1: Simple 2x3 matrix
data1 = [[2, 4, 6], [1, 2, 3]]
soln1 = [[1, 2, 3], [0, 0, 0]]

# Test Case 2: 3x3 identity matrix (should remain unchanged)
data2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
soln2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# Test Case 3: Matrix that reduces to identity
data3 = [[2, 4, 6], [1, 3, 5], [0, 1, 2]]
soln3 = [[1, 0, -1], [0, 1, 2], [0, 0, 0]]

# Test Case 4: Matrix with zero row
data4 = [[1, 2, 3], [0, 0, 0], [2, 4, 6]]
soln4 = [[1, 2, 3], [0, 0, 0], [0, 0, 0]]

# Test Case 5: 2x2 matrix
data5 = [[3, 6], [1, 2]]
soln5 = [[1, 2], [0, 0]]

# Test Case 6: Matrix requiring row swapping
data6 = [[0, 1, 2], [1, 0, 3], [2, 1, 4]]
soln6 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# Test Case 7: 4x3 matrix (more rows than columns)
data7 = [[1, 2, 3], [2, 4, 6], [1, 1, 1], [0, 1, 2]]
soln7 = [[1, 0, -1], [0, 1, 2], [0, 0, 0], [0, 0, 0]]

# Test Case 8: 2x4 matrix (more columns than rows)
data8 = [[1, 2, 3, 4], [2, 4, 7, 9]]
soln8 = [[1, 2, 0, 1], [0, 0, 1, 1]]

# Test Case 9: Matrix with negative numbers
data9 = [[-2, 4, -6], [1, -2, 3], [3, -6, 9]]
soln9 = [[1, -2, 3], [0, 0, 0], [0, 0, 0]]

# Test Case 10: Matrix with fractions/decimals
data10 = [[0.5, 1.0, 1.5], [1.0, 2.0, 4.0], [1.5, 3.0, 6.0]]
soln10 = [[1, 2, 0], [0, 0, 1], [0, 0, 0]]

# Test Case 11: 3x4 augmented matrix style
data11 = [[1, 1, 1, 6], [1, 2, 3, 14], [2, 1, 1, 10]]
soln11 = [[1, 0, 0, 4], [0, 1, 0, -4], [0, 0, 1, 6]]

# Test Case 12: Matrix that becomes zero matrix
data12 = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
soln12 = [[1, 2, 3], [0, 0, 0], [0, 0, 0]]

# Test Case 13: Single row matrix
data13 = [[3, 6, 9, 12]]
soln13 = [[1, 2, 3, 4]]

# Test Case 14: Single column matrix
data14 = [[2], [4], [6]]
soln14 = [[1], [0], [0]]

# Test Case 15: All zero matrix
data15 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soln15 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Run all test cases
print("Running RREF Tests...")
print("Test 1:", end=" ")
test(data1, soln1)
print("Test 2:", end=" ")
test(data2, soln2)
print("Test 3:", end=" ")
test(data3, soln3)
print("Test 4:", end=" ")
test(data4, soln4)
print("Test 5:", end=" ")
test(data5, soln5)
print("Test 6:", end=" ")
test(data6, soln6)
print("Test 7:", end=" ")
test(data7, soln7)
print("Test 8:", end=" ")
test(data8, soln8)
print("Test 9:", end=" ")
test(data9, soln9)
print("Test 10:", end=" ")
test(data10, soln10)
print("Test 11:", end=" ")
test(data11, soln11)
print("Test 12:", end=" ")
test(data12, soln12)
print("Test 13:", end=" ")
test(data13, soln13)
print("Test 14:", end=" ")
test(data14, soln14)
print("Test 15:", end=" ")
test(data15, soln15)
print("All RREF tests completed!")
