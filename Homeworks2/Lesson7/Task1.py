"""

1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.

Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

"""


class Matrix:
    def __init__(self, list_matrix):
        self.__list_matrix = list_matrix

    def __str__(self):
        return str("\n".join(["\t".join([str(i) for i in j]) for j in self.__list_matrix]))

    def __add__(self, other):
        self.__temp_list = []
        self.__result_matrix = []
        for i in range(len(self.__list_matrix)):
            for j in range(len(self.__list_matrix[i])):
                self.__temp_list.append(self.__list_matrix[i][j] + other.__list_matrix[i][j])
            self.__result_matrix.append(self.__temp_list)
            self.__temp_list = []
        return Matrix(self.__result_matrix)


a1 = Matrix([[31, 22],
             [37, 43],
             [51, 86]])
b1 = Matrix([[131, 122],
             [137, 143],
             [151, 186]])
c1 = (a1 + b1)

print("Матрицы 3 на 2:")
print("Первая матрица:")
print(a1)
print("Вторая матрица:")
print(b1)
print("Сумма матриц:")
print(c1)

a2 = Matrix([[3, 5, 32],
             [2, 4, 6],
             [-1, 64, -8]])
b2 = Matrix([[23, 25, 232],
             [22, 24, 26],
             [-21, 264, -28]])
c2 = (a2 + b2)

print()
print("Матрицы 3 на 3:")
print("Первая матрица:")
print(a2)
print("Вторая матрица:")
print(b2)
print("Сумма матриц:")
print(c2)

a3 = Matrix([[3, 5, 8, 3],
             [8, 3, 7, 1]])
b3 = Matrix([[33, 35, 38, 33],
             [38, 33, 37, 31]])
c3 = (a3 + b3)

print()
print("Матрицы 2 на 4:")
print("Первая матрица:")
print(a3)
print("Вторая матрица:")
print(b3)
print("Сумма матриц:")
print(c3)