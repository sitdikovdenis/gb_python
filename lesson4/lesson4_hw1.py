"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

import sys
from sys import argv

from pathlib import Path
path = Path(__file__).parent.parent
sys.path.append(str(path) + "\check_functions")

from check_functions import is_float

script_name, first_param, second_param, third_param = argv


def salary(hours, rate, premium):
    args = (hours, rate, premium)
    for arg in args:
        if not is_float(arg):
            print(f"Параметр {arg} должен был вещественным числом")
            return
    salary_total = (float(hours) * float(rate)) + float(premium)
    print(f"Сотрудник получит {salary_total} руб.")
    return salary_total


salary(first_param, second_param, third_param)
