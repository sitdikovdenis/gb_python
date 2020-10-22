"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

russian_name_of_numbers = {'1': "один",
                           '2': "два",
                           '3': "три",
                           '4': "четыре",
                           '5': "пять",
                           '6': "шесть",
                           '7': "семь",
                           '8': "восемь",
                           '9': "девять"}


with open("l5_hw4.txt", 'r', encoding="utf-8") as numbers:
    with open("l5_hw4_new.txt", 'a', encoding="utf-8") as f_obj:
        for line in numbers:
            english_name = line.split('-')[0].strip()
            number = line.split('-')[1].strip()
            f_obj.write(f"{number} - {russian_name_of_numbers[number]}\n")
