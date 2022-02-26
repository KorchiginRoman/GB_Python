from functools import wraps


def val_checker(func):
    def checker(func_0):
        @wraps(func_0)
        def decor(x):
            if func(x):
                return func_0(x)
            raise ValueError(f'ValueError: wrong val {x}')

        return decor

    return checker


@val_checker(lambda x: x > 0)  # не забудьте про аргумент-функцию
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube(0))
