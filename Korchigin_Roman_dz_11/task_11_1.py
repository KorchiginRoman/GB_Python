class Date:
    def __unit__(self, requested_date):
        self.requested_date = requested_date

    # def __str__(self) -> str:
    #    return f'Текущая дата {Date.extract_date(self.requested_date)}'

    # classmethod — это метод, который привязан к классу, а не к экземпляру класса.
    @classmethod
    def extract_date(cls, requested_date):
        try:
            return list(map(int, requested_date.split("-")))
        except:
            raise ValueError("Невозможно произвести произвести операцию")

    # статический метод не может изменять состояние ни объекта, ни класса. Виды данных, которые могут принимать
    # статические методы, ограничены. Эти методы помещаются в класс, просто чтобы они находились в пространстве
    # имен этого класса, т. е., для организационных целей.
    @staticmethod
    def valid_date(day, month, year):
        if month in [2, 4, 6, 9, 11] and day == 31:
            return f'Возвращайтесь в садик и учите количество дней в месяцах!'

        if month in [2] and day == 30:
            return f'К сожалению 30 февраля не существует!'

        if (
                month == 2 and
                day == 29 and
                year % 4 != 0
        ):
            return f'Упс! Не Високосный год!'

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2050 >= year >= 1:
                    return f'Формат данных правильный!'
                else:
                    return f'Проверьте правильность введения параметра "год"!'
            else:
                return f'Проверьте правильность введения параметра "месяц"!'
        else:
            return f'Проверьте правильность введения параметра "день"!'


if __name__ == '__main__':
    print(Date.extract_date('11 - 3 - 2022'))
    print(Date.valid_date(30, 2, 2022))
