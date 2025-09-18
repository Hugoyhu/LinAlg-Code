# Matrix class for creating and storing 2D integer matrices, with eq, str, and the elementary row operations.

from tabulate import tabulate


class Matrix:
    def __init__(self, data):
        """
        Initialize Matrix w/ 2D list data.
        Checks for empty matrices.
        Uses 0 indexing.
        """
        if len(data) == 0:
            raise Exception("Empty Matrix")

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
