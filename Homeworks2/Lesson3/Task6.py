"""

6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
возвращающую их же, но с прописной первой буквой.

Например, print(int_func(‘text’)) -> Text.

"""


def my_func(s):
    return s.capitalize()


print(my_func("text"))