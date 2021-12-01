def thesaurus(*args):
    names = {}
    for name in args:
        N = name[0]
        if N in names:
            names[N] += [name]
        else:
            names[N] = [name]
    return names.items()

print(thesaurus("Иван", "Мария", "Петр", "Илья"))




