import os
import shutil

cur_folder = 'my_project'

#os.path.realpath(path) - возвращает канонический путь, убирая все символические ссылки (если они поддерживаются).
#os.path.join(path1[, path2[, ...]]) - соединяет пути.
#Метод endwith() возвращает True, если строка заканчивается указанным суффиксом. Если нет, возвращается False.
#Функция split() модуля os.path делит путь path на двойной кортеж (head, tail),
#где tail - это последний компонент имени пути, а head - это все остальное.
#real_path = os.path.relpath(os.path.join(root, file), cur_folder)
#print(real_path)
files = [os.path.relpath(os.path.join(root, file), cur_folder) for root, _, files in os.walk(
    cur_folder) for file in files if file.endswith(".html")]
for rel_path in files:
    path, file = os.path.split(rel_path)
    template_path = os.path.join(cur_folder, "template", path)
    if not os.path.exists(template_path):
        os.makedirs(template_path)
    shutil.copyfile(os.path.join(cur_folder, rel_path), os.path.join(template_path, file))
#Функция copyfile() модуля shutil копирует содержимое файла, без метаданных.


