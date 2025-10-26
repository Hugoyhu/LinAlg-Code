# Computing -- Matrices and Lists, Due 09/22

import matpy


def is_zero_row(data):
    flag = True
    for x in data:
        if x != 0:
            flag = False
            break
    return flag


def solve_RREF(data: matpy.Matrix, row_counter=0, col_counter=0):
    """
    Input matrix of size m x n, solve using Gauss-Jordan elimination. Recursive.
    """

    k = row_counter
    s = col_counter

    # data = Matrix(d)
    num_rows = data.num_rows()
    num_cols = data.num_cols()

    # check if recursion has ended
    if k >= num_rows:
        return

    entry = data.return_entry(k, s)

    # Is (k, s) zero?
    if data.return_entry(k, s) == 0:
        # flag to check if entries found
        flag = False

        # check rows below k for non-zero entry in col s.
        for r in range(k + 1, num_rows):
            if data.return_entry(r, s) != 0:
                # first row w/ non-zero col s entry found, interchange & break.
                data.interchange_rows(r, k)
                flag = True
                break
        if not flag:
            # no non-zero entries found. call next interation
            solve_RREF(data, k + 1, s + 1)
    else:
        # multiply row k by reciprocal of entry in (k, s)
        reciprocal = 1 / (entry)
        data.scale_row(k, reciprocal)

        # for each row below k, add multiple of row k (with pivot = 1) to make initial pivot 0.
        for r in range(k + 1, num_rows):
            curr_entry = data.return_entry(r, s)
            if curr_entry != 0:
                data.add_linear_multiple(r, k, (-1) * curr_entry)

        solve_RREF(data, k + 1, s + 1)

    # now, push the 0 rows down inefficiently
    for a in range(num_rows):
        for b in range(a, num_rows - 1):
            row = data.return_row(b)
            if is_zero_row(row):
                data.interchange_rows(b, b + 1)

    # now, make every row pivot the only pivot in that row
    # iterate over columns, then by rows (above)
    for a in range(1, min(num_cols, num_rows)):
        for b in range(0, a):
            entry = data.return_entry(b, a)
            if entry != 0:
                data.add_linear_multiple(b, a, (-1) * entry)

    return
