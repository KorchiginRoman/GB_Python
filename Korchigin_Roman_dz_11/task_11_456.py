class Warehouse:
    def __init__(self):
        self.my_warehouse: set = set()

    def download_equipment(self, *args):
        count = 0
        for equipment in args:
            if not isinstance(equipment, OfficeEquipment):
                print(f'Внимание! Передают товар, не для хранения на нашем складе!')
                continue
            self.my_warehouse.add(equipment)
            count += 1
        print(f'Оборудование из магазина добавлено на склад! Количество наименований прибывшего товара: {count} ')


class OfficeEquipment:
    def __init__(self, name, price, quantity, my_store: set):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.my_store = my_store
        self.my_store.add(self)
        print(f'Обнаруженное оборудование. Модель: {self.name}. Цена: {self.price} руб.'
              f' Количество: {self.quantity}')

    def __str__(self) -> str:
        return f'Модель: {self.name}. Цена: {self.price} руб. Количество: {self.quantity}'

    # def __setattr__(self, key, value):
    #    if key == 'price'or 'quantity' and isinstance(value, int):
    #        self.__dict__[key] = value
    #    else:
    #        print(f'Значение {key} недопустимо')

    def __add__(self, other):
        my_money = self.price * self.quantity + other.price * other.quantity
        print(f'Для заполнения прилавков мне понадобится {my_money} руб.')


class Printer(OfficeEquipment):
    def __init__(self, name, price, quantity, my_store: set):
        super().__init__(name, price, quantity, my_store)
        self.paper = str(input(f'Введите формат поддерживаемой бумаги: '))

    def format(self):
        return f'Формат поддерживаемой бумаги {self.paper}.'


class Scanner(OfficeEquipment):
    def __init__(self, name, price, quantity, my_store: set):
        super().__init__(name, price, quantity, my_store)
        self.perm = int

    def permission(self):
        try:
            self.perm = int(input(f'Введите максимальное разрешение сканера: '))
            return f'Разрешение данного сканера {self.perm} dpi.'
        except ValueError:
            return f'Вы ввели не число'


class Monitor(OfficeEquipment):
    def __init__(self, name, price, quantity, my_store: set):
        super().__init__(name, price, quantity, my_store)
        self.param = int

    def inch(self):
        try:
            self.param = int(input(f'Введите диагональ монитора: '))
            return f'Диагональ монитора {self.param} дюйм.'
        except ValueError:
            return f'Вы ввели не число'


class Mouse(OfficeEquipment):
    pass


if __name__ == '__main__':
    my_warehouse = set()
    print('В магазине намечается ремонт. Необходимо провести ревизию.')
    equip_1 = Printer('HP', 14000, 3, my_warehouse)
    print(equip_1.format())
    # model_1 = Printer('A4', 1000, 15)
    # print(Printer.print_1(model_1))
    equip_2 = Scanner('Canon', 5200, 3, my_warehouse)
    print(equip_2.permission())
    equip_3 = Monitor('Benq', 12150, 3, my_warehouse)
    print(equip_3.inch())
    print(f'Перечень оборудования в магазине:')
    for eqiup in my_warehouse:
        print(f'\t{eqiup}')
    # print(f'{equip_2}')
    # equip_1 + equip_3
    print('Чтобы не испачкать оборудование, перемещаем его на склад.')
    warehouse = Warehouse()
    warehouse.download_equipment(*my_warehouse)
    equip_4 = Mouse('Aceline', 1000, 5, warehouse.my_warehouse)
    equip_5 = Printer('Epson', 13000, 2, warehouse.my_warehouse)
    for eqiup in warehouse.my_warehouse:
        print(f'\t{eqiup}')
