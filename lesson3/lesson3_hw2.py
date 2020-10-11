def print_user_info(name, surname, birthday, city, email, phone):
    """
    функция получает на вход данные о пользователе и выводит информацию о пользователе
    :param name: имя
    :param surname: фамилия
    :param birthday: год рождения
    :param city: город проживания
    :param email: email
    :param phone: телефон
    :return: None
    """
    print(f"Пользователь {surname} {name} {birthday} года рождения. Проживает в городе {city}. Email: {email}, "
          f"телефон: {phone}")


user_name = input("Введите имя: ")
user_surname = input("Введите фамилию: ")
user_birthday = input("Введите год рождения: ")
user_city = input("Введите город проживания: ")
user_email = input("Введите email: ")
user_phone = input("Введите телефон: ")

print_user_info(surname=user_surname, name=user_name, birthday=user_birthday, city=user_city, email=user_email,
                phone=user_phone)
