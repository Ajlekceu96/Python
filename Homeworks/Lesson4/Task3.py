"""

Задайте последовательность чисел.
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

"""

list_simple = list(map(int, input("Введите числа через пробел: ").split()))
print(f"Исходный список: {list_simple}")
print(f"Результат: {list(set(list_simple))}")
