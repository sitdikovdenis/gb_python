# задание 5
proceeds = input("Введите выручку: ")
costs = input("Введите издержки: ")

proceeds = int(proceeds)
costs = int(costs)

delta = proceeds - costs

if delta < 0:
    print("Фирма работает с убытком")
elif delta > 0:
    rent = delta / proceeds
    print("Фирма работает с прибылью. Рентабельность: %.2f%% " % (rent*100))
    people_count = input("Введите численность сотрудников фирмы: ")
    people_count = int(people_count)
    print("Прибыль фирмы в расчете на одного сотрудника: %.2f" % (delta/people_count))
else:
    print("Фирма работает в ноль")
