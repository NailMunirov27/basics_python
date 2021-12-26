import re


def email_parse(email_address):
    username_domain = re.compile(r'(?P<username>\w+)@(?P<domain>\w+\.\w+)', re.IGNORECASE)

    if not "." in str(email_address).split('@')[1]:
        raise ValueError("wrong email: " + str(email_address))
    print(username_domain.match(email_address).groupdict())


email_parse('someWone23@geekbrains.ru')
