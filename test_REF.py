import matrix


def test(data, answer):
    """
    Test RREF function with data input and soln output
    """
    m = matrix.Matrix()
    m.list_dataloader(data)
    res = m.is_REF()
    print(res == answer)


# below test cases were written with Github Copilot, Claude Sonnet 5.

# Test Case 1: Simple 2x2 matrix in REF
data1 = [[1, 2], [0, 1]]
answer1 = True

# Test Case 2: 2x2 matrix NOT in REF (pivot in wrong position)
data2 = [[0, 1], [1, 2]]
answer2 = False

# Test Case 3: 3x3 identity matrix (perfect REF)
data3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
answer3 = True

# Test Case 4: 3x3 matrix with zero row at bottom (valid REF)
data4 = [[1, 2, 3], [0, 1, 4], [0, 0, 0]]
answer4 = True

# Test Case 5: 3x3 matrix with zero row in middle (invalid REF)
data5 = [[1, 2, 3], [0, 0, 0], [0, 1, 4]]
answer5 = False

# Test Case 6: Single row matrix (always REF)
data6 = [[1, 2, 3, 4]]
answer6 = True

# Test Case 7: Matrix with leading 1s in correct staircase pattern
data7 = [[1, 2, 0, 3], [0, 0, 1, 4], [0, 0, 0, 1]]
answer7 = True

# Test Case 8: Matrix where pivot is not to the right of previous pivot
data8 = [[1, 2, 3], [0, 0, 1], [0, 1, 0]]
answer8 = False

# Test Case 9: All zero matrix (technically REF)
data9 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
answer9 = True

# Test Case 10: Rectangular matrix 2x4 in proper REF
data10 = [[1, 3, 0, 5], [0, 0, 1, 2]]
answer10 = True

# Test Case 11: Single column matrix (always REF)
data11 = [[1], [0], [0]]
answer11 = True

# Test Case 12: Matrix with negative pivots (still valid REF)
data12 = [[-1, 2, 3], [0, -2, 1], [0, 0, -3]]
answer12 = True

# Test Case 13: Matrix where first row is all zeros (invalid REF)
data13 = [[0, 0, 0], [1, 2, 3], [0, 0, 1]]
answer13 = False

# Test Case 14: 4x4 matrix in perfect staircase REF
data14 = [[1, 2, 3, 4], [0, 1, 5, 6], [0, 0, 1, 7], [0, 0, 0, 1]]
answer14 = True

# Test Case 15: Matrix with fractional entries in REF
data15 = [[1, 0.5, 0], [0, 1, 0.25], [0, 0, 1]]
answer15 = True

# Test Case 16: Wide matrix 2x5 with skipped columns (valid REF)
data16 = [[1, 0, 2, 0, 3], [0, 0, 0, 1, 4]]
answer16 = True

# Test Case 17: Matrix with zero pivot position causing invalid REF
data17 = [[1, 2, 3], [0, 0, 4], [0, 0, 0], [0, 1, 0]]
answer17 = False

# Test Case 18: Tall matrix 5x2 in REF
data18 = [[1, 2], [0, 1], [0, 0], [0, 0], [0, 0]]
answer18 = True

# Test Case 19: Matrix where second pivot is in same column as first (invalid)
data19 = [[1, 0, 2], [0, 0, 0], [1, 0, 3]]
answer19 = False

# Test Case 20: Single element matrix (always REF)
data20 = [[5]]
answer20 = True

# Run all test cases
print("Running REF Tests...")
print("Test 1:", end=" ")
test(data1, answer1)
print("Test 2:", end=" ")
test(data2, answer2)
print("Test 3:", end=" ")
test(data3, answer3)
print("Test 4:", end=" ")
test(data4, answer4)
print("Test 5:", end=" ")
test(data5, answer5)
print("Test 6:", end=" ")
test(data6, answer6)
print("Test 7:", end=" ")
test(data7, answer7)
print("Test 8:", end=" ")
test(data8, answer8)
print("Test 9:", end=" ")
test(data9, answer9)
print("Test 10:", end=" ")
test(data10, answer10)
print("Test 11:", end=" ")
test(data11, answer11)
print("Test 12:", end=" ")
test(data12, answer12)
print("Test 13:", end=" ")
test(data13, answer13)
print("Test 14:", end=" ")
test(data14, answer14)
print("Test 15:", end=" ")
test(data15, answer15)
print("Test 16:", end=" ")
test(data16, answer16)
print("Test 17:", end=" ")
test(data17, answer17)
print("Test 18:", end=" ")
test(data18, answer18)
print("Test 19:", end=" ")
test(data19, answer19)
print("Test 20:", end=" ")
test(data20, answer20)
print("All tests completed!")
