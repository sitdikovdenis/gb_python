"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class NotDigitException(ValueError):
    def __init__(self, str):
        print(f"{str} должен быть типа isdigit!")


my_list = []
list_item = ""

while list_item != "q":
    list_item = input("Введите значение для списка. Для прекращения введите символ 'q':")
    if list_item != 'q':
        my_list.append(list_item)

try:
    for elem in my_list:
        if not elem.isdigit():
            raise NotDigitException(elem)
except NotDigitException:
    pass
