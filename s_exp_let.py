from s_pair import *


def let(name, value, body):
    return pair("let", pair(name, pair(value, pair(body, empty_pair))))


def is_let(x):
    return is_pair(x) and first(x) == "let"


def let_name(l):
    return first(second(l))


def let_value(l):
    return first(second(second(l)))


def let_body(l):
    return first(second(second(second(l))))
