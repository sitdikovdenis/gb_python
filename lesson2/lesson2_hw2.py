my_list = []
list_item = ""

while list_item != ".":
    list_item = input("Введите значение для списка. Для прекращения введите символ '.':")
    my_list.append(list_item)

print(my_list)

i = 1
while i < len(my_list):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
    i += 2

print(my_list)
