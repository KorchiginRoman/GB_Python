def convert_name_extract(list_in: list) -> list:
    list_out = []
    for i in list_in:
        hello = (f"Привет, {i.split()[-1].title()}!")
        list_out.append(hello)
    return list_out

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)

# for i in my_list:
#   print(f"Привет, {i.split()[-1].title()}!")