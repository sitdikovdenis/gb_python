my_list = [7, 5, 3, 3, 2]
print(my_list)

rating = ''
while rating != "exit":
    try:
        rating = input("Введите новый элемент рейтинга (целое число). Для выхода наберите exit: ")
        rating = int(rating)
        my_list.append(rating)
        my_list.sort(reverse=True)
        print(my_list)
    except ValueError:
        if rating != 'exit':
            rating = ''
