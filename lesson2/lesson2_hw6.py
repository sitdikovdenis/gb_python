reference = []

update_ref = 'Д'
i = 1
while update_ref == 'Д':
    # проверку на типы вводимых данных не делаем, потому что аналитик не расписал что там может быть указано
    name = input("Название товара: ")
    cost = input("Цена товара: ")
    count = input("Количество: ")
    uom = input("Единица измерения: ")
    input_dict = {"название": name,
                  "цена": cost,
                  "количество": count,
                  "eд": uom}

    record = (i, input_dict)
    reference.append(record)
    i += 1
    update_ref = input("Продолжить заполнять справочник? Д/Н ")

print(reference)

# собрать аналитику
# аналитик не указал, нужно ли собирать уникальные наименования, поэтому собираем все,
# хоть в примере и указана одна единица измерения
# если что потом добавим проверку if index = 0
names = []
costs = []
counts = []
uoms = []

for record in reference:
    names.append(record[1]["название"])
    costs.append(record[1]["цена"])
    counts.append(record[1]["количество"])
    uoms.append(record[1]["eд"])

    analytics = ({"название": names,
                  "цена": costs,
                  "количество": counts,
                  "eд": uoms})

print(analytics)
