# импортируем модуль sys. Нам понадобиться метод argv возвращает аргументы командной строки,
# переданные скрипту Python, в виде списка.
import sys

input_prices = list(map(lambda price: f"{float(price):<10.2f}", filter(
    lambda price: price.replace('.', '').isdigit(), sys.argv[1:])))

file_name = 'bakery.csv'
with open(file_name, "a", encoding="utf-8") as price_1:
    print(*input_prices, sep="\n", file=price_1)

