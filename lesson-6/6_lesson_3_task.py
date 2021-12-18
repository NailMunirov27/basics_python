from itertools import zip_longest
from json import dump

with open('hobby.csv', 'r+', encoding='utf-8') as hobby:
    with open('users.csv', 'r+', encoding='utf-8') as users:

        if len(users.readlines()) >= len(hobby.readlines()):
            users.seek(0)
            hobby.seek(0)

            with open('hobby_list.csv', 'w', encoding='utf-8') as hobby_list:
                h_l = zip_longest((" ".join(us.split(',')) for us in users), hobby, fillvalue=None)
                my_dict = {str(el[0]).strip(): str(el[1]).strip() for el in h_l}

                dump(my_dict, hobby_list, ensure_ascii=False, indent=4)
            print(my_dict)
        else:
            exit(666)