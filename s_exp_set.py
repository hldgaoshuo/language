from s_pair import *


def set_exp(name, value, body):
    return pair("set", pair(name, pair(value, pair(body, empty_pair))))


def is_set(x):
    return is_pair(x) and first(x) == "set"


def set_name(s):
    return first(second(s))


def set_value(s):
    return first(second(second(s)))


def set_body(s):
    return first(second(second(second(s))))
