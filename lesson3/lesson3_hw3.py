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


def my_func(num1, num2, num3):
    """
    функция возвращает сумму наибольших двух аргументов.
    :param num1: число, тип данных float
    :param num2: число, тип данных float
    :param num3: число, тип данных float
    :return: сумма наибольших двух аргументов
    """
    nums = [num1, num2, num3]
    return sum(nums) - min(nums)


num1 = ''
while not is_digit(num1):
    num1 = input("Введите первое число: ")

num1 = float(num1)

num2 = ''
while not is_digit(num2):
    num2 = input("Введите второе число: ")

num2 = float(num2)

num3 = ''
while not is_digit(num3):
    num3 = input("Введите третье число: ")

num3 = float(num3)

print(my_func(num1, num2, num3))
