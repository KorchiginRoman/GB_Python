from typing import Any, Generator


def odd_nums(number: int) -> Generator[int, Any, None]:
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
    return (elem for elem in range(1, number + 1, 2))


n = 24
generator = odd_nums(n)
for _ in range(1, n + 1, 2):
    print(next(generator))