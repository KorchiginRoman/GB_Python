import requests


def currency_rates(code: str) -> float | None:
    """возвращает курс валюты `code` по отношению к рублю"""
    # ваша реализация здесь
    code = code.upper()
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url)
    value_cbr = response.text
    # if not (code and url):
    #   return None
    if response.ok:
        course = value_cbr.split(code)
        if len(course) == 1:
            return
        value = course[1].split("</Value>")[0].split("<Value>")[1]
        value = float(value.replace(",", "."))
        nominal = course[1].split("</Nominal>")[0].split("<Nominal>")[1]
        nominal = float(nominal.replace(",", "."))
    else:
        return
    # Round — встроенная функция Python. Ее задача — округлять число с плавающей точкой до той цифры, которую задает
    # пользователь
    result_value = round(value / nominal, 5)
    return result_value


print(currency_rates("USD"))
print(currency_rates("gth"))
