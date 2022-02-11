import requests


def currency_rates(code: str) -> float | None:
    code = code.upper()
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url)
    value_cbr = response.text
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
    result_value = round(value / nominal, 5)
    return result_value

