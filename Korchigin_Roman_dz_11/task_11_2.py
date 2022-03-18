class Division(Exception):
    def __unit__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    @staticmethod
    def excep():
        try:
            dividend = int(input(f'Введите делимое:'))
            divider = int(input(f'Введите делитель:'))
            if divider == 0:
                return f'Делить на ноль нельзя!'
            else:
                result: float = dividend / divider
                return result
        except ValueError:
            return f'Вы ввели не число'


print(Division.excep())
