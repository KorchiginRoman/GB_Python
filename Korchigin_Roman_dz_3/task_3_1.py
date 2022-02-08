# создаем словарь для обращения в дальнейшем к нему
number_dic = {

    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",

}


def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    str_out = number_dic.get(value)
    return str_out


print(num_translate("two"))
print(num_translate("eight"))
