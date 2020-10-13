special_symbol = 'q'
not_found = -1


def my_sum(*args):
    """
    Функция возвращает сумму чисел, переданных в качестве параметра.
    :param args: список чисел
    :return: сумма чисел
    """

    args_list = [float(num) for num in args]
    args_sum = sum(args_list)
    return args_sum


def string_check(string_for_check):
    """
    Функция проверяет входную строку на заданное услвие
    :param string_for_check: строка
    :return: если на вход подана строка чисел с разделителем либо символ 'q', то True. Иначе False
    """
    if string_for_check == special_symbol:
        return True
    else:
        string_for_check = string_for_check.replace(' ', '')
        string_for_check = string_for_check.replace(special_symbol, '')
        try:
            float(string_for_check)
            return True
        except ValueError:
            return False


sum_of_input_num = 0
input_str = "1"

while input_str.find(special_symbol) == not_found:
    input_str = input("Введите строку чисел, разделенных пробелом: ")
    if string_check(input_str):
        result_string = input_str.split(special_symbol)[0]
        sum_of_input_num += my_sum(*result_string.split())
        print(sum_of_input_num)
    else:
        input_str = "1"
