def thesaurus(*args) -> dict:
    # пишите свою реализацию здесь
    dict_out = {}  # результирующий словарь значений

    for name in args:

        if dict_out.get(
                name[0]):  # Метод get() возвращает значение для указанного ключа, если ключ находится в словаре.
            dict_out[name[0]].append(name)  # Метод append() добавляет элемент в конец списка.
        else:
            dict_out[name[0]] = [name]

    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Роман", "Андрей"))
