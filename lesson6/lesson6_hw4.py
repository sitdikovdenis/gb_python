"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print("Сбавьте скорость!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(self.speed)
        if self.speed > 40:
            print("Сбавьте скорость!")


class PoliceCar(Car):
    pass


t_car = TownCar(61, 'red', 'name1', False)
t_car.go()
t_car.show_speed()
t_car.speed = 50
t_car.show_speed()
t_car.turn("направо")
t_car.stop()
