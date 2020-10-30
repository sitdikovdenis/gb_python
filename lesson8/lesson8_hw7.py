"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""

class Complex:
    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __mul__(self, other):
        return Complex((self.r * other.r - self.i * other.i), (self.i * other.r + self.r * other.i))


c1 = Complex(1, -1)
c2 = Complex(3, 6)
c3 = c1 * c2
print(c3.r, c3.i)
