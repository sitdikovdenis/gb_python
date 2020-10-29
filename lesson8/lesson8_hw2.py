"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""

class SuperPuperZeroDivisionError(ZeroDivisionError):
    def __init__(self):
        print("На но(у)ль делить нельзя!!!!")


numerator = 100

denominator = input(f"Введите число, на которое мы разделим {numerator}: ")
if denominator == '0':
    raise SuperPuperZeroDivisionError

print(numerator/int(denominator))
