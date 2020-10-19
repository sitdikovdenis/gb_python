def is_float(string):
    """
    проверят является ли строка числом
    :param string: строка, которую необходимо проверить
    :return: True, если строка является числом, False иначе
    """
    try:
        float(string)
        return True
    except ValueError as err:
        print(f"Ошибка, переданное значение {string} не является вещественным числом. \nПодробнее: {err}")
        return False
