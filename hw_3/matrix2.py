import numpy as np

class FileIOMixin:
    def save_to_file(self, filename):
        np.savetxt(filename, self.data, fmt="%d")

    def load_from_file(self, filename):
        self.data = np.loadtxt(filename, dtype=int)

class DisplayMixin:
    def __str__(self):
        return str(self.data)

class GetterSetterMixin:
    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = np.array(data)

class ArithmeticMixin:
    def __add__(self, other):
        return type(self)(self.data + other.data)

    def __mul__(self, other):
        return type(self)(self.data * other.data)

    def __matmul__(self, other):
        return type(self)(np.matmul(self.data, other.data))

class Matrix(ArithmeticMixin, FileIOMixin, DisplayMixin, GetterSetterMixin):
    def __init__(self, data):
        self.data = np.array(data)
        self.shape = self.data.shape

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
