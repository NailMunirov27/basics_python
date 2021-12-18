from sys import argv

with open('bakery.csv', 'a', encoding='utf-8') as bul_a:
    with open('bakery.csv', 'r', encoding='utf-8') as bul_r:
        if len(argv) > 1 and [i for i in argv[1:] if '.' in i and i.replace('.', '').isdigit()]:
            if round(float(argv[1]), 3) <= 99999.999:
                print(f'{round(float(argv[1]), 3):>010}', file=bul_a)
            else:
                print('nope')
        else:
            print(bul_r.read())
