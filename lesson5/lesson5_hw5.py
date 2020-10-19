"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random


with open("l5_hw5.txt", 'w', encoding="utf-8") as f_obj:
    for i in range(20):
        random_num = random.randint(0, 100)
        f_obj.write(f"{random_num} ")

# В новом контексте, чтоб изменения сохранились
with open("l5_hw5.txt", 'r', encoding="utf-8") as f_obj:
    line = f_obj.readline()
    num_sum2 = sum([int(num) for num in line.split()])

print(f"Сумма чисел в файле {num_sum2}")

