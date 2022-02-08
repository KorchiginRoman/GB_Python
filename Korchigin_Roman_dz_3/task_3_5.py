from random import choice  # из модуля random импортируем функцию choice (возвращает случайный элемент списка)

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    # пишите реализацию своей программы здесь
    list_out = []
    # for i in range(count):
    #    noun = choice(nouns)
    #    adv = choice(adverbs)
    #    adj = choice(adjectives)
    # f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}"
    for joke in range(count):
        list_out.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
    # list_out = list(zip(noun, adv, adj))
    # if len(nouns) and len(adverbs) and len(adjectives) > 5:
    #    return []
    return list_out


print(get_jokes(3))
print(get_jokes(20))

# result = zip(nouns, adverbs, adjectives)
# print(tuple(result))
