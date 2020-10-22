"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

import pathlib
current_path = pathlib.Path().absolute()

lesson5_hw1_file_name = "l5_hw1.txt"

with open(lesson5_hw1_file_name, 'a') as f_obj:
    input_str = "1"
    while input_str:
        input_str = input("Enter data: ")
        if input_str:
            f_obj.write(f"{input_str}\n")

