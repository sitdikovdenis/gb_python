"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


class MatrixIterator:
    def __init__(self, matrix, start=-1):
        self.matrix = matrix
        self.i = start

    def __next__(self):
        self.i += 1
        if self.i < len(self.matrix):
            return self.matrix[self.i]
        else:
            raise StopIteration

class Matrix:
    def __init__(self, data):
        self.m = data

    def __iter__(self):
        return MatrixIterator(self.m)

    def __str__(self):
        def search_max_len(data):
            max_len = 0
            for line in data:
                for item in line:
                    if len(str(item)) > max_len:
                        max_len = len(str(item))
            return max_len

        matrix_view = ""
        max_len = search_max_len(self.m)
        for line_of_matrix in self.m:
            # для ровного вывода дополнить число пробелами до максимальной длины
            split_line = '|'.join([str(elem) + " " * (max_len - len(str(elem))) for elem in line_of_matrix])
            matrix_view = '\n'.join([matrix_view,  split_line])
        return matrix_view

    def __add__(self, other):
        return Matrix([[x + y for x, y in zip(m1, m2)] for m1, m2 in zip(self, other)])


list1 = [[1, 1, 1], [2, 2, 2]]
list2 = [[4, 4, 4], [5, 5, 5]]

m1 = Matrix(list1)
print(m1)
m2 = Matrix(list2)
print(m2)

for asda in m1:
    print(asda)

m3 = m1 + m2
print(m3)