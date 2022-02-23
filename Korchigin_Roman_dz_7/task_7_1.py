import os

folders = {
    'my_project': [
        {
            'settings': [],
            'mainapp': [],
            'adminapp': [],
            'authapp': [],
            'testapp':[{'test_1': []}]
        }]
}

def creator(pth, data):
    for folder, project in data.items():
        #os.path.join(path1[, path2[, ...]]) - соединяет пути с учётом особенностей операционной системы.
        path = os.path.join(pth, folder)
        # os.path.exists(path) - возвращает True, если path указывает на существующий путь или дескриптор открытого файла.
        if not os.path.exists(path):
            os.mkdir(path)
        if len(project) > 0:
            for proj in project:
                creator(path, proj)

#Функция getcwd() модуля os вернет строку, представляющую текущий рабочий каталог.
creator(os.getcwd(),data=folders)


