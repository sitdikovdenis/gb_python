"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.
"""

import time
from termcolor import colored


class TrafficLight:
    # время работы каждого цвета
    time_of_work = {"red": 7, "yellow": 2, "green": 6}
    default_sleep_time = 1
    __color = ""
    __current_color = "current_color"

    # зададим порядок следования цветов в светофоре
    correct_color_order = ["red", "yellow", "green"]

    def check_color_correct_order(self, old_color, current_color):
        if old_color != "current_color":
            if self.correct_color_order.index(current_color) - self.correct_color_order.index(old_color) != 1:
                raise Exception("Нарушен порядок светофора")
        return True

    def running(self, color):
        if color in self.correct_color_order:
            if self.check_color_correct_order(old_color=self.__current_color, current_color=color):
                try:
                    print(colored("⚫", color))
                except KeyError:
                    print(color)
                self.__color = color
                self.__current_color = color
                try:
                    time.sleep(self.time_of_work[color])
                except KeyError:
                    time.sleep(self.default_sleep_time)
        else:
            raise Exception(f"Светофор сломался, доступные цвета: {self.correct_color_order}")


colors = ["red", "yellow", "green"]

tl = TrafficLight()
for color in colors:
    tl.running(color)
