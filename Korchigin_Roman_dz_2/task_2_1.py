a = 15 * 3
# print(a)
print(type(a))

a = 15 / 3
# print(a)
print(isinstance(a, float))

a = 15 // 2
# print(a)
if not isinstance(a, str):
    print('Нам нужно любое значение, кроме строчки. Условие выполнено.')

a = 15 ** 2
print(type(a) == float)
