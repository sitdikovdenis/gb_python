def my_division(num1, num2):
    """
    :param num1: первое число, тип данных - float
    :param num2: второе число, тип данных - float
    :return: результат деления первого числа на второе. Если num2 = 0, то выводится строка что на ноль делить нельзя
    и возвращается None
    """
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
        raise ZeroDivisionError


def is_digit(string):
    """
    проверят является ли строка числом
    :param string: строка, которую необходимо проверить
    :return: True, если строка является числом, False иначе
    """
    try:
        float(string)
        return True
    except ValueError:
        return False


num1 = ''
while not is_digit(num1):
    num1 = input("Введите первое число: ")

num1 = float(num1)

num2 = ''
while not is_digit(num2):
    num2 = input("Введите второе число: ")

num2 = float(num2)

div_result = my_division(num1, num2)
print(f"num1 / num2 = {div_result}")
