# Декоратор `@wraps()` модуля `functools` это функция для вызова `@functools.update_wrapper()`
# в качестве декоратора при определении функции-обертки.
# Декоратор `@update_wrapper()` модуля `functools` обновляет функцию-обертку, чтобы она выглядела
# как исходная функция.
from functools import wraps


def type_logger(number):
    def logger(func):

        @wraps(func)
        def decor(*argv):
            if number > 0:
                return 'calc_cube(' + ", ".join([f"{x}:{type(x)}" for x in argv]) + ")"
            else:
                return "calc_cube(" + ", ".join([str(x) for x in argv]) + ")"

        return decor

    return logger


@type_logger(1)
def calc_cube(x):
    """ cube of args """
    return x ** 3


a = calc_cube(5, 6)
print(a)
