"""

Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и
выведите в формате чч:мм:сс. Используйте форматирование строк.

"""

date = int(input("Введите время в секундах: "))
h = str(date // 3600).rjust(2, "0")
m = str((date % 3600) // 60).rjust(2, "0")
s = str((date % 3600) % 60).rjust(2, "0")

print(f"{h}:{m}:{s}")
