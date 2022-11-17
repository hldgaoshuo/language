from s_pair import *


def while_exp(cond, then, final):
    return pair("while", pair(cond, pair(then, pair(final, empty_pair))))


def is_while(x):
    return is_pair(x) and first(x) == "while"


def while_cond(i):
    return first(second(i))


def while_then(i):
    return first(second(second(i)))


def while_final(i):
    return first(second(second(second(i))))
