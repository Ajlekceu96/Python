"""

Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение
Формат: Объясняет преподаватель

Задача: предложить улучшения кода для уже решённых задач:

С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
В этом случае можно пропустить совсем тривиальные
(т.е. задачу 1 или 2 тут точно решать не имеет смысла) - исходите из уровня группы и студента.


За основу взят Урок 3 Задача 1

Задайте список из нескольких чисел.
Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

"""


list_simple: list[int] = [2, 3, 5, 9, 3]
print(f"Список = {list_simple}")
print(f"Результат = {sum([list_simple[i] for i in range(1, len(list_simple), 2)])}")
