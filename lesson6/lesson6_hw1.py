"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.
"""

import time
from termcolor import colored

class TrafficLight():
    # время работы каждого цвета
    time_of_work = {"red": 7, "yellow": 2, "green": 6}
    __color = "red"
    __current_color = __color

    correct_color_order = ["red", "yellow", "green"]

    def check_color_correct_order(self, old_color, current_color):
        print(self.correct_color_order.index(current_color) - self.correct_color_order.index(old_color))
        if self.correct_color_order.index(current_color) - self.correct_color_order.index(old_color) != 1 :
            raise Exception("Нарушен порядок светофора")

    def running(self, color):
        if self.check_color_correct_order(old_color=self.__current_color, current_color=color):
            print(colored("⚫", color))
            self.__color = color
            self.__current_color = color
            time.sleep(self.time_of_work[color])

colors = ["red", "yellow", "green"]

tl = TrafficLight()
for color in colors:
    tl.running(color)
