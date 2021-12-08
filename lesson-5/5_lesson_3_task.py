from itertools import zip_longest, islice

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б']

rez = (name for name in zip_longest(tutors, klasses) if len(tutors) > len(klasses))

print(list(rez))
print(type(rez))
print(*islice(rez, 5))