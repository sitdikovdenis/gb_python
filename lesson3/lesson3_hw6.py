#решение без str.title

def int_func(string):
    """
    функция принимает слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой
    :param string:
    :return:
    """
    return string.capitalize()


str1 = input("Введите слово: ")
print(int_func(str1))

str2 = input("Введите строку из слов, разделенных пробелом: ")
res_str = ""
for word in str2.split():
    a = int_func(word)
    res_str = " ".join([res_str, a])

print(res_str)
