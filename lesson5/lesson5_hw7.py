"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

company_with_profit_count = 0
total_profit = 0
company_dict = {}

with open("l5_hw7_company.json", "w") as json_f:
    with open("l5_hw7.txt", 'r', encoding="utf-8") as f_obj:
        for line in f_obj:
            company_list = line.split()
            company_name = company_list[0]
            company_ownership_type = company_list[1]
            company_income = company_list[2]
            company_spending = company_list[3]
            profit = int(company_income) - int(company_spending)
            company_dict.update({company_name: profit})
            if profit > 0:
                total_profit += profit
                company_with_profit_count += 1

    if company_with_profit_count > 0:
        company_dict.update({"average_profit": total_profit/company_with_profit_count})

    json.dump(company_dict, json_f)

print(json)