with open('nginx_logs.txt', 'r+', encoding='utf-8') as parse:
    r = ((k.split()[0], k.split()[5], k.split()[6]) for k in parse)

    for line in r:
        print(line)

