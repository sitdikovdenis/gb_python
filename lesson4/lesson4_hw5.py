"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce

my_list = [elem for elem in range(100, 1001) if elem % 2 == 0]

print(my_list)


def my_mult(prev_el, el):
    return prev_el * el


print(reduce(my_mult, my_list))
