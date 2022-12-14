"""

7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное
значение. При вызове функции должен создаваться объект-генератор. Функция вызывается
следующим образом: for el in fact(n). Она отвечает за получение факториала числа. В цикле
нужно выводить только первые n чисел, начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал
четырёх 4! = 1 * 2 * 3 * 4 = 24.

"""

from itertools import count
from math import factorial


def fibo_gen():
    for j in count(1):
        yield factorial(j)


gen = fibo_gen()
x = 1
for i in gen:
    if x < 10:
        print(f"!{x} = {i}")
        x += 1
    else:
        break
