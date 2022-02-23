import os

result = {}
path_0 = os.getcwd()
# print(path_0)

def scan_folder(path_0):
    if not os.path.exists(path_0):
        return
    # os.scandir() в Python используется для получения итератора объектов os.DirEntry,
    # соответствующих записям в каталоге, заданным указанным путем.
    with os.scandir(path_0) as files:
        for file in files:
            # Функция isfile() модуля os.path возвращает True если путь path существует и является обычным файлом,
            # False в противном случае.
            if os.path.isfile(file):
                mem = 10 ** len(str(os.stat(file).st_size))
                result[mem] = result.get(mem, 0) + 1
            # Функция isdir() модуля os.path возвращает True если путь path существует и является каталогом,
            # False в противном случае.
            elif os.path.isdir(file):
                scan_folder(os.path.join(path_0, file))


scan_folder(path_0)
finish_result = dict(sorted(result.items()))
print(finish_result)
