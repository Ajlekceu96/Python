"""

Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение
Формат: Объясняет преподаватель

Задача: предложить улучшения кода для уже решённых задач:

С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
В этом случае можно пропустить совсем тривиальные
(т.е. задачу 1 или 2 тут точно решать не имеет смысла) - исходите из уровня группы и студента.


За основу взят Урок 2 Задача 1

Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

- 6782 -> 23
- 0,56 -> 11

"""

num = input("Введите число: ")
print(f"Сумма цифр = {sum([int(i) for i in num if i.isdigit()])}")
