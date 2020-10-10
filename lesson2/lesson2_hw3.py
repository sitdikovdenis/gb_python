month = 0
while month < 1 or month > 12:
    try:
        month = input("Введите  месяц в виде целого числа от 1 до 12: ")
        month = int(month)
    except ValueError:
        month = 0

# решение используя list
seasons_list = ["зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима"]
print(seasons_list[month-1])

# решение используя dict
# по идее словарь вида {зима:1, зима:2} будет работать быстрее, но да ладно
seasons_dict = {"зима": [12, 1, 2], "весна": [3, 4, 5], "лето": [6, 7, 8], "осень": [9, 10, 11]}
for season_name, season_index in seasons_dict.items():
    if month in season_index:
        print(f"точно {season_name}!")
        break
