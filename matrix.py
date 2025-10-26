# Matrix class for creating and storing 2D integer matrices, with eq, str, and the elementary row operations.

from tabulate import tabulate
import csv


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

        # data = Matrix(d)
        num_rows = self.data.num_rows()
        num_cols = self.data.num_cols()

        # check if recursion has ended
        if k >= num_rows:
            return

        entry = self.data.return_entry(k, s)

        # Is (k, s) zero?
        if self.data.return_entry(k, s) == 0:
            # flag to check if entries found
            flag = False

            # check rows below k for non-zero entry in col s.
            for r in range(k + 1, num_rows):
                if self.data.return_entry(r, s) != 0:
                    # first row w/ non-zero col s entry found, interchange & break.
                    self.data.interchange_rows(r, k)
                    flag = True
                    break
            if not flag:
                # no non-zero entries found. call next interation
                self.solve_RREF(k + 1, s + 1)
        else:
            # multiply row k by reciprocal of entry in (k, s)
            reciprocal = 1 / (entry)
            self.data.scale_row(k, reciprocal)

            # for each row below k, add multiple of row k (with pivot = 1) to make initial pivot 0.
            for r in range(k + 1, num_rows):
                curr_entry = self.data.return_entry(r, s)
                if curr_entry != 0:
                    self.data.add_linear_multiple(r, k, (-1) * curr_entry)

            self.solve_RREF(k + 1, s + 1)

        # now, push the 0 rows down inefficiently
        for a in range(num_rows):
            for b in range(a, num_rows - 1):
                row = self.data.return_row(b)
                if self.is_zero_row(row):
                    self.data.interchange_rows(b, b + 1)

        # now, make every row pivot the only pivot in that row
        # iterate over columns, then by rows (above)
        for a in range(1, min(num_cols, num_rows)):
            for b in range(0, a):
                entry = self.data.return_entry(b, a)
                if entry != 0:
                    self.data.add_linear_multiple(b, a, (-1) * entry)

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
