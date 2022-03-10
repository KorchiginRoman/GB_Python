from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        lenght_m = len(matrix[0])
        for row in matrix:
            if len(row) != lenght_m:
                raise ValueError('fail initialization matrix')
        self.matrix = matrix

    def __str__(self):
        for row in self.matrix:
            for i in row:
                print(f"{i} ", end="")
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for k in range(len(other.matrix[i])):
                self.matrix[i][k] += other.matrix[i][k]
        return Matrix.__str__(self)


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
    second_matrix = Matrix([[6, 5, 4], [4, 3, 6], [2, 1, 6]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """
