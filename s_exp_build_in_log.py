from s_pair import *


def log_exp(arg, final):
    return pair("log", pair(arg, pair(final, empty_pair)))


def is_log(x):
    return is_pair(x) and first(x) == "log"


def log_arg(l):
    return first(second(l))


def log_final(l):
    return first(second(second(l)))
