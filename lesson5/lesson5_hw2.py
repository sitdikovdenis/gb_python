"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

file_name = "l5_hw2.txt"

with open(file_name, 'r') as f_obj:
    line_count = 0
    word_count = 0
    for line in f_obj:
        line_count += 1
        word_count = len(line.split())
        print(f"В строке {line_count} {word_count} слов")

print(f"Всего {line_count} строк")
