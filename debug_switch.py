import matrix

def debug_test(data, test_name, expected):
    """Debug a specific test case"""
    print(f"\n=== {test_name} ===")
    print("Input:")
    for row in data:
        print(row)
    
    # Test with regular RREF
    m1 = matrix.Matrix()
    m1.list_dataloader([row[:] for row in data])  # Deep copy
    m1.solve_RREF()
    print("\nRegular RREF Result:")
    for row in m1.data:
        formatted_row = [round(x, 6) for x in row]
        print(formatted_row)
    
    # Test with switch RREF
    m2 = matrix.Matrix()
    m2.list_dataloader([row[:] for row in data])  # Deep copy
    m2.solve_switch_RREF()
    print("\nSwitch RREF Result:")
    for row in m2.data:
        formatted_row = [round(x, 6) for x in row]
        print(formatted_row)
    
    print("\nExpected:")
    for row in expected:
        print(row)
    
    # Compare
    expected_matrix = matrix.Matrix()
    expected_matrix.list_dataloader(expected)
    
    print(f"\nRegular RREF matches expected: {m1 == expected_matrix}")
    print(f"Switch RREF matches expected: {m2 == expected_matrix}")
    print(f"Both methods match each other: {m1 == m2}")

# Test Case 8
data8 = [[1, 2, 3, 4], [2, 4, 7, 9]]
soln8 = [[1, 2, 0, 1], [0, 0, 1, 1]]
debug_test(data8, "Test 8", soln8)

# Test Case 10
data10 = [[0.5, 1.0, 1.5], [1.0, 2.0, 4.0], [1.5, 3.0, 6.0]]
soln10 = [[1, 2, 0], [0, 0, 1], [0, 0, 0]]
debug_test(data10, "Test 10", soln10)