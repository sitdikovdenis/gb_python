def my_division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("На ноль делить нельзя!")


def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


num1 = ''
while not is_digit(num1):
    num1 = input("Введите первое число: ")

num1 = float(num1)

num2 = ''
while not is_digit(num2):
    num2 = input("Введите второе число: ")

num2 = float(num2)

div_result = my_division(num1, num2)
print(f"num1 / num2 = {div_result}")
