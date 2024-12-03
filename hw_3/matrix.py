import numpy as np

class Matrix:
    def __init__(self, data):
        self.data = np.array(data)
        self.shape = self.data.shape

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError("Матрицы должны иметь одинаковый размер для сложения")
        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if self.shape != other.shape:
            raise ValueError("Матрицы должны иметь одинаковый размер для поэлементного умножения")
        return Matrix(self.data * other.data)

    def __matmul__(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы для матричного умножения")
        return Matrix(np.matmul(self.data, other.data))

    def __str__(self):
        return str(self.data)

    def save_to_file(self, filename):
        np.savetxt(filename, self.data, fmt='%d')


if __name__ == "__main__":
    np.random.seed(0)
    matrix1_data = np.random.randint(0, 10, (10, 10))
    matrix2_data = np.random.randint(0, 10, (10, 10))

    matrix1 = Matrix(matrix1_data)
    matrix2 = Matrix(matrix2_data)

    matrix_sum = matrix1 + matrix2
    matrix_mul_elementwise = matrix1 * matrix2
    matrix_mul_matrix = matrix1 @ matrix2

    matrix_sum.save_to_file("matrix+.txt")
    matrix_mul_elementwise.save_to_file("matrix*.txt")
    matrix_mul_matrix.save_to_file("matrix@.txt")
