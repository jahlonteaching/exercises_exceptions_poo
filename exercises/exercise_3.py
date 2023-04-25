class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0 for j in range(columns)] for i in range(rows)]

    def __str__(self):
        return '\n'.join([' '.join([str(self.data[i][j]) for j in range(self.columns)]) for i in range(self.rows)])

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError('Matrices must have the same dimensions to be added.')
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError('Matrices must have the same dimensions to be subtracted.')
        result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    def __mul__(self, other):
        if self.columns != other.rows:
            raise ValueError(
                'The number of columns in the first matrix must match the number of rows in the second matrix to be multiplied.')
        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result
