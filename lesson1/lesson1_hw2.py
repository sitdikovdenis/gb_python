# задание 2
second_count = input("Введите время в секундах: ")
second_count = int(second_count)
second_count_2 = second_count

# посчитать часы минуты и секунды отдельно:
hours = int(second_count / 3600)

second_count = second_count - (hours * 3600)
minutes = int(second_count / 60)

second_count = second_count - (minutes * 60)

print("%02d:%02d:%02d" % (hours, minutes, second_count))

# используем только форматирование без привидения типов в переменных
print("%02d:%02d:%02d" % (second_count_2 / 3600, (second_count_2 / 60) % 60, second_count_2 % 60))
