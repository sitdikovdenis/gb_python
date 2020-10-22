from check_functions.check_functions import is_float

"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

"""
    Информация о сотрудниках хранится в csv файле, разделитель " "
"""


def employee_check(employee_info):
    try:
        employee_surname = employee_info.split()[0]
        employee_salary = employee_info.split()[1]
        return is_float(employee_salary)
    except IndexError as ind_err:
        print(f"Ошибка в формате файла, не указаны имя или фамилия.\n Подробнее: {ind_err}")
        return False


start_salary = 20000
emp_count = 0
salary_sum = 0

with open("l5_hw3.txt", 'r', encoding="utf-8") as employees:
    for employee in employees:
        if employee_check(employee):
            employee_surname = employee.split()[0]
            employee_salary = employee.split()[1]
            employee_salary = float(employee_salary)
            salary_sum += employee_salary
            emp_count += 1
            if employee_salary < start_salary:
                print(f"{employee_surname} получает меньше {start_salary} рублей.")

if emp_count > 0:
    print(f"Средняя зарлата на предприятии {salary_sum / emp_count} рублей")
