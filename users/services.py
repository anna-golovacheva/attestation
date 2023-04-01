import re


def num_in_password(password):
    regexp = re.compile(r".{0,}\d{1,}.{0,}")
    m = regexp.match(password)
    return m


def email_domain(email):
    regexp = re.compile(r"(.){1,}(@mail\.ru$|@yandex.ru)")
    m = regexp.match(email)
    return m
