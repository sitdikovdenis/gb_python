def my_func(x, y):
    """
    функция возводит число x в степень y используя оператор **
    :param x:
    :param y:
    :return:
    """
    return x ** y


def is_positive_digit(string):
    """
    проверят является ли строка положительным действительным числом
    :param string: строка, которую необходимо проверить
    :return: True, если строка является числом, False иначе
    """
    try:
        num = float(string)
        if num >= 0:
            return True
        else:
            return False
    except ValueError:
        return False


x = ''
while not is_positive_digit(x):
    x = input("Введите действительное положительное число x: ")

x = float(x)

y = "1"
while int(y) > 0:
    try:
        y = int(input("Введите целое отрицательное число y: "))
    except ValueError:
        pass

print(my_func(x, y))


def my_func2(x, y):
    if y == 0:
        return 1
    if y == -1:
        return 1. / x
    p = my_func2(x, y // 2)
    p *= p
    if y % 2:
        p *= x
    return p


print(my_func2(x, y))
