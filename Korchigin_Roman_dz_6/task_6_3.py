import sys
import json
from itertools import zip_longest


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    # Ваш код пишите здесь
    # path_users_file = "./users.csv"
    # path_hobby_file = "./hobby.csv"
    # if (path_users_file or path_hobby_file):
    #    return -1
    # users = []
    # hobby = []
    with open(path_users_file, "r", encoding="utf-8") as user_file, open(path_hobby_file, "r",
                                                                         encoding="utf-8") as hobby_file:
        # Метод файла file.readlines() читает файловый объект file построчно.
        user = []
        hobby_1 = []
        users = user_file.readlines()
        # print(users)
        for i in users:
            user.append(i.replace(",", " ").replace("\n", ""))

        hobby = hobby_file.readlines()
        for i_2 in hobby:
            hobby_1.append(i_2.replace("\n", "") if hobby else None)
        if len(users) < len(hobby):
            sys.exit(1)
        return dict(zip_longest(user, hobby_1))  # верните словарь, либо завершите исполнение программы кодом 1


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
