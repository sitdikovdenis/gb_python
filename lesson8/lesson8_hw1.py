"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

from _datetime import datetime


class InvalidDateException(ValueError):
    def __init__(self, txt, *args, **kwargs):
        super().__init__(txt)


class Date:
    def __init__(self, date):
        if self.date_validation(date):
            Date.date = date
        else:
            # наверно с точки зрения разделения ответственности не совсем правильынй подход рейзить тут исключение,
            # но очень хотелось попробовать свое
            raise InvalidDateException("Неправильная дата епт")

    @classmethod
    def date_to_int(cls):
        return [int(e) for e in cls.date.split("-")]

    @staticmethod
    def date_validation(date):
        try:
            datetime.strptime(date, "%d-%m-%Y")
            return True
        except Exception:
            return False


date_obj = Date("29-02-2021")

date_attr_list = date_obj.date_to_int()
print(date_attr_list)
