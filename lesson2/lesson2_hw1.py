my_list = [1, 2, 3, 'one', 'two', 'three', True]
my_list.append('str from append')

for elem in my_list:
    print(f"Элемент '{elem}' имеет тип {type(elem)}")
