def is_float(string):
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
