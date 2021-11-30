from random import randrange, choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(r, repeat=False):

    """
    Генератор случайных шуток из имеющихся списков.

    :param r: количество шуток
    :param repeat: наличие уникальных шуток
    :return: список сгенерированных шуток

    """

    joke_rand = []
    list_min = min(nouns, adverbs, adjectives)

    while r and len(list_min):
        num = randrange(len(list_min))
        if repeat:
            joke_rand.append(f"{nouns.pop(num)} {adverbs.pop(num)} {adjectives.pop(num)}")
        else:
            joke_rand.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        r -= 1

    return joke_rand

print(get_jokes(4, True))