import re


def email_parse(email: str) -> None:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    # Функция compile() модуля re компилирует шаблон регулярного выражения pattern в объект регулярного выражения,
    # который может быть использован для поиска совпадений с использованием методов Match.match(), Match.search()
    # и других способов.
    RE_MAIL = re.compile(r'(?P<username>([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+)@(?P<domain>[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+)')
    # пишите реализацию здесь
    match_email = RE_MAIL.match(email)
    if not match_email:
        raise ValueError
    # Метод Match.groupdict() возвращает словарь, содержащий все именованные подгруппы совпадения,
    # помеченные именем подгруппы name.
    finish_mail = match_email.groupdict()
    return print(finish_mail)


if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrainsru')
