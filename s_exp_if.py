from s_pair import *


def if_exp(cond, then, else_exp, final):
    return pair("if", pair(cond, pair(then, pair(else_exp, pair(final, empty_pair)))))


def is_if(x):
    return is_pair(x) and first(x) == "if"


def if_cond(i):
    return first(second(i))


def if_then(i):
    return first(second(second(i)))


def if_else_exp(i):
    return first(second(second(second(i))))


def if_final(i):
    return first(second(second(second(second(i)))))
