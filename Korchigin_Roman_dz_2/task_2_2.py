def convert_list_in_str(list_in: list) -> str:
    str_out = ''
    length_list: int = len(my_list)
    for i in range(length_list):
        new_list = my_list.pop(0)
        if new_list.isdigit() and new_list.isalnum():  # Метод isdigit() возвращает True, если все символы в строке являются цифрами. Если нет, возвращается False.
            my_list.append(f'"{int(new_list):02d}"')
        elif new_list[0] == "+" and new_list[1].isdigit():
            my_list.append(f'"+{int(new_list):02d}"')
        else:
            my_list.append(new_list)
    str_out = (' '.join(my_list))
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)

