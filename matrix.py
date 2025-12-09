# Matrix class for creating and storing 2D integer matrices, with eq, str, and the elementary row operations.

from tabulate import tabulate
import csv
import math
import numpy as np


class Matrix:
    def __init__(self):
        self.data = [[0]]

    def list_dataloader(self, data):
        """
        Initialize Matrix w/ 2D list data.
        Checks for empty matrices.
        Uses 0 indexing.
        """
        if len(data) == 0:
            raise Exception("Empty Matrix")

        for col in range(len(data)):
            for row in range(len(data[col])):
                data[col][row] = float(data[col][row])

        self.data = data

    def csv_dataloader(self, path):
        """
        Initialize Matrix from csv.
        Floats okay.
        Code is based off Mr. Honner's Import_Matrix code.
        https://github.com/stuyphonner/LinAlg2025-26/blob/main/Importing_Matrices.py
        """

        with open(path) as f:
            reader = csv.reader(f)
            data = list(reader)

        for col in range(len(data)):
            for row in range(len(data[col])):
                data[col][row] = float(data[col][row])

        self.data = data

    def __str__(self):
        """
        String representation of the matrix.
        """
        return tabulate(self.data)

    def __eq__(self, other: "Matrix"):
        if not isinstance(other, Matrix):
            return False
        if (self.num_rows() != other.num_rows()) or (
            self.num_cols() != other.num_cols()
        ):
            return False
        for a in range(self.num_rows()):
            for b in range(self.num_cols()):
                if self.data[a][b] != other.data[a][b]:
                    return False
                # if not math.isclose(self.data[a][b], other.data[a][b], rel_tol=1e-9):
                #     return False

        return True

    def num_rows(self):
        return len(self.data)

    def num_cols(self):
        return len(self.data[0])

    def checkRowOOB(self, row):
        if (row < 0) or (row >= len(self.data)):
            raise Exception("Row OOB")

    def checkRowColOOB(self, row, col):
        self.checkRowOOB(row)
        if (col < 0) or (col >= len(self.data[0])):
            raise Exception("Column OOB")

    def checkKOOB(self, c):
        if c == 0:
            raise Exception("c cannot be 0.")

    def is_zero_row(self, row):
        flag = True
        for x in self.data[row]:
            if x != 0:
                flag = False
                break
        return flag

    def return_row(self, row):
        """
        Returns specific row in matrix.
        """
        self.checkRowOOB(row)
        return self.data[row]

    def return_entry(self, row, col):
        """
        Returns specific entry in matrix.
        """
        self.checkRowColOOB(row, col)
        return self.data[row][col]

    def scale_row(self, row, c):
        """
        Scales a specific row by c.
        """
        self.checkRowOOB(row)
        self.checkKOOB(c)

        for entry_ref in range(len(self.data[row])):
            self.data[row][entry_ref] *= c

    def interchange_rows(self, row1, row2):
        """
        Interchanges row1, row2.
        """
        self.checkRowOOB(row1)
        self.checkRowOOB(row2)

        temp_row = self.return_row(row1)
        self.data[row1] = self.data[row2]
        self.data[row2] = temp_row

    def add_linear_multiple(self, changed_row, added_row, c):
        """
        Add k * added_row to changed_row.
        """
        self.checkRowOOB(changed_row)
        self.checkRowOOB(added_row)
        self.checkKOOB(c)

        for entry_ref in range(len(self.data[added_row])):
            self.data[changed_row][entry_ref] += self.data[added_row][entry_ref] * c

    def solve_RREF(self, row_counter=0, col_counter=0):
        """
        Input matrix of size m x n, solve using Gauss-Jordan elimination. Recursive.
        """

        k = row_counter
        s = col_counter

        num_rows = self.num_rows()
        num_cols = self.num_cols()

        # check if recursion has ended
        if k >= num_rows or s >= num_cols:
            return

        # Is (k, s) zero?
        if abs(self.return_entry(k, s)) < 1e-10:
            # flag to check if entries found
            flag = False

            # check rows below k for non-zero entry in col s.
            for r in range(k + 1, num_rows):
                if abs(self.return_entry(r, s)) > 1e-10:
                    # first row w/ non-zero col s entry found, interchange & break.
                    self.interchange_rows(r, k)
                    flag = True
                    break
            if not flag:
                # no non-zero entries found. call next iteration with next column
                self.solve_RREF(k, s + 1)
                return

        # multiply row k by reciprocal of entry in (k, s)
        entry = self.return_entry(k, s)
        if abs(entry) > 1e-10:
            reciprocal = 1 / entry
            self.scale_row(k, reciprocal)

            # for each row below k, add multiple of row k (with pivot = 1) to make initial pivot 0.
            for r in range(k + 1, num_rows):
                curr_entry = self.return_entry(r, s)
                if abs(curr_entry) > 1e-10:
                    self.add_linear_multiple(r, k, (-1) * curr_entry)

        self.solve_RREF(k + 1, s + 1)

        # After forward elimination, do backward elimination
        # Move zero rows to bottom
        for a in range(num_rows - 1):
            for b in range(a, num_rows - 1):
                if self.is_zero_row(b) and not self.is_zero_row(b + 1):
                    self.interchange_rows(b, b + 1)

        # Make every pivot the only non-zero entry in its column (backward elimination)
        for row in range(min(num_rows, num_cols) - 1, -1, -1):
            # Find pivot column for this row
            pivot_col = -1
            for col in range(num_cols):
                if abs(self.return_entry(row, col)) > 1e-10:
                    pivot_col = col
                    break

            if pivot_col != -1:
                # Eliminate entries above this pivot
                for r in range(row):
                    entry = self.return_entry(r, pivot_col)
                    if abs(entry) > 1e-10:
                        self.add_linear_multiple(r, row, (-1) * entry)

        return

    def solve_switch_RREF(self, row_counter=0, col_counter=0):
        """
        Input matrix of size m x n, solve using Gauss-Jordan elimination. Recursive.
        This modified version switches rows with lots of zeroes closer to the bottom.
        """

        k = row_counter
        s = col_counter

        # data = Matrix(d)
        num_rows = self.num_rows()
        num_cols = self.num_cols()

        # check if recursion has ended
        if k >= num_rows or s >= num_cols:
            return

        # go through each remaining row starting at k, s to "swap" zeroes to bottom
        curr_row = k
        last_unswapped = num_rows - 1
        while curr_row < last_unswapped:
            entry = self.return_entry(curr_row, s)
            # if 0, swap with last_unswapped and decrement last unswapped
            # if not 0, increment row
            if entry == 0:
                self.interchange_rows(curr_row, last_unswapped)
                last_unswapped -= 1
            else:
                curr_row += 1

        entry = self.return_entry(k, s)

        # Is (k, s) zero?
        if self.return_entry(k, s) == 0:
            # flag to check if entries found
            flag = False

            # check rows below k for non-zero entry in col s.
            for r in range(k + 1, num_rows):
                if self.return_entry(r, s) != 0:
                    # first row w/ non-zero col s entry found, interchange & break.
                    self.interchange_rows(r, k)
                    flag = True
                    break
            if not flag:
                # no non-zero entries found. call next interation
                self.solve_switch_RREF(k + 1, s + 1)
                return
        else:
            # multiply row k by reciprocal of entry in (k, s)
            reciprocal = 1 / (entry)
            self.scale_row(k, reciprocal)

            # for each row below k, add multiple of row k (with pivot = 1) to make initial pivot 0.
            for r in range(k + 1, num_rows):
                curr_entry = self.return_entry(r, s)
                if curr_entry != 0:
                    self.add_linear_multiple(r, k, (-1) * curr_entry)

            self.solve_switch_RREF(k + 1, s + 1)
            return

        # now, push the 0 rows down inefficiently
        for a in range(num_rows):
            for b in range(a, num_rows - 1):
                # row = self.return_row(b)
                if self.is_zero_row(b):
                    self.interchange_rows(b, b + 1)

        # now, make every row pivot the only pivot in that row
        # iterate over columns, then by rows (above)
        for a in range(1, min(num_cols, num_rows)):
            for b in range(0, a):
                entry = self.return_entry(b, a)
                if entry != 0:
                    self.add_linear_multiple(b, a, (-1) * entry)

        return

    def is_REF(self):
        # iterates over each row, keeping track of "last pivot".
        # also checks if zero-rows have started.

        last_pivot = -1
        zero_row_reached = False

        for row in range(self.num_rows()):
            is_zero = self.is_zero_row(row)
            for col in range(self.num_cols()):
                if self.data[row][col] != 0:
                    if col <= last_pivot:
                        # this means that the pivot isn't to the right of previous!
                        return False
                    last_pivot = col
                    break

            if zero_row_reached and not is_zero:
                return False

            zero_row_reached = is_zero

        return True

    def matrix_dimensions(self):
        num_rows = len(self.data)
        num_cols = len(self.data[0])
        return (num_rows, num_cols)

    def can_multiply_matrices(self, N: "Matrix"):
        # you can multiply matrices M and N if M: axb and N: bxc

        # check columns of M (self):
        m_size = self.matrix_dimensions()

        # check rows of N:
        n_size = N.matrix_dimensions()

        return m_size[1] == n_size[0]

    def matrix_product_entry(self, N: "Matrix", i, j):
        if not self.can_multiply_matrices(N):
            raise Exception("Matrices cannot be multiplied")
        # returns float

        # row[0]*col[0] + row[1]*col[1] + ... row[n]*col[n]

        sum = 0
        for k in range(len(N.data)):
            sum += (float(self.data[i][k])) * float((N.data[k][j]))

        return sum

    def multiply(self, N: "Matrix"):
        """
        Returns the matrix that results from multiplication of self and input.
        An exception will be raised if the matrices cannot be multiplied.
        """
        if not self.can_multiply_matrices(N):
            raise Exception("Matrices cannot be multiplied")

        # determine output size
        numRows = self.matrix_dimensions()[0]
        numCols = N.matrix_dimensions()[1]

        # create an empty matrix of mxn 0s
        outData = np.zeros((numRows, numCols))

        # iterate over rows then columns, finding each entry
        for i in range(numRows):
            for j in range(numCols):
                outData[i][j] = self.matrix_product_entry(N, i, j)

        out = Matrix()
        out.list_dataloader(outData)

        return out

    def transpose(self):
        """
        Returns the transposition of the matrix.
        """
        dim = self.matrix_dimensions()
        numRows = dim[0]
        numCols = dim[1]

        # create an empty matrix of nxm 0s
        outData = np.zeros((numCols, numRows))

        for i in range(numRows):
            for j in range(numCols):
                outData[j][i] = self.data[i][j]

        return outData

    def output_galois_field(self):
        # converts input matrix M to a Matrix over Z_2
        # in other words, we take modulo 2 on every entry.

        dim = self.matrix_dimensions()
        numRows = dim[0]
        numCols = dim[1]

        # create an empty matrix of mxn 0s
        outData = np.zeros((numRows, numCols))

        # iterate over rows then columns, finding each entry
        for i in range(numRows):
            for j in range(numCols):
                outData[i][j] = self.data[i][j] % 2

        return outData

    def field_multiply(self, N: "Matrix"):
        # multiplies then converts to matrix under z_2
        # for any a, b: (a%2)*(b%2)= (a*b) %2.

        out = self.multiply(N)

        return out.output_galois_field()
