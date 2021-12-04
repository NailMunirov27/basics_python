from requests import get, utils
from datetime import date

all_rubbish = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))


def currency_rates(val):
    content = all_rubbish.split('<Valute ID=')
    d, m, y = map(int, content[0].split('"')[-4].split('.'))
    print(date(year=y, month=m, day=d), end=', ')

    for i in content:
        if val.upper() in i:
            print(val.upper(), end='-RUB ')
            return float(i.replace('/', '').split('<Value>')[-2].replace(',', '.'))