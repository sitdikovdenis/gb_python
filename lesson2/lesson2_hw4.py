strings = input("Введите строку из нескольких слов, разделённых пробелами: ")

i = 1
for string in strings.split():
    print(i, string[:10])
    i += 1
