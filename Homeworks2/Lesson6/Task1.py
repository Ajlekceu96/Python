"""

1. Создать класс TrafficLight (светофор).
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт.

"""

from time import sleep


class TrafficLight:
    __color = ["Красный", "Желтый", "Зеленый"]

    def running(self):
        i = 0
        while i < 6:
            print(f"{TrafficLight.__color[i % 3]}")
            if i % 3 == 0:
                j = 7
                while j >= 1:
                    print(f"{j}...", end="")
                    if j == 1:
                        print()
                    j -= 1
                    sleep(1)
            elif i % 3 == 1:
                j = 2
                while j >= 1:
                    print(f"{j}...", end="")
                    if j == 1:
                        print()
                    j -= 1
                    sleep(1)
            elif i % 3 == 2:
                j = 5
                while j >= 1:
                    print(f"{j}...", end="")
                    if j == 1:
                        print()
                    j -= 1
                    sleep(1)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()
