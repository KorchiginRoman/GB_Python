from random import uniform

my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
        #"Первое задание"

#   """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
#       формирует из них единую строковую переменную разделяя значения запятой."""

def transfer_list_in_str(list_in: list) -> str:
    str_out = ""
    for i, num in enumerate(my_list): #Функция enumerate() вернет кортеж, содержащий отсчет от start и значение, полученное из итерации по объекту.
         fix_price = str(f"{float(num):.2f}").split(".")
         str_out += f" {fix_price[0]} руб {fix_price[1]} коп,"
    return str_out



print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)

    #"Второе задание"

def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    # пишите реализацию здесь
    list_in.sort()
    return list_in


print(id(my_list))# зафиксируйте здесь информацию по исходному списку my_list
result_2 = sort_prices(my_list)
print(id(result_2))# зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
print(result_2)

    #"Третье задание"

def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    list_out = sorted(list_in, reverse=True) #reverse=True - в обратном порядке
    dir(list_out)
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)

    #"Четвертое задание"

def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    list_out = sorted(list_in, reverse=True)[:5]
    dir(list_out)
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)
