# Комплексное число — это выражение вида a + bi, где a, b — действительные числа,
# а i — так называемая мнимая единица,
# символ, квадрат которого равен –1, то есть i2 = –1.
class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # сумма двух комплексных чисел (a1+a2)+(b1+b2)i
    def __add__(self, other):
        return f'Сумма двух комплексных чисел равна: {self.a + other.a} + {self.b + other.b}*i'

    # произведение двух комплексных чисел равно (a1*a2 - b1*b2)+(a2*b1 + a1*b2)*i
    def __mul__(self, other):
        return f'Произведение двух комплексных чисел равно:{self.a * other.a - self.b * other.b} +' \
               f' {self.b * other.a + self.a * other.b}*i'


z_1 = ComplexNumber(89, 14)
z_2 = ComplexNumber(13, 8)
print(z_1 + z_2)
print(z_1 * z_2)
