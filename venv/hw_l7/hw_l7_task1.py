class Matrix:
    def __init__(self, list : list):
        self.list = list

    def __str__(self):
        return "\n".join(map(str, self.list))

    def __add__(self, other):
        for i in range(len(self.list)):
            for n in range(len(self.list[i])):
                self.list[i][n] = self.list[i][n] + other.list[i][n]
        return Matrix.__str__(self)

matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix_1, "\n", "**********")
matrix_2 = Matrix([[-1, -3, -5], [0, -7, 5], [3, -2, 4]])
print(matrix_2, "\n", "**********")
print(matrix_1 + matrix_2)

