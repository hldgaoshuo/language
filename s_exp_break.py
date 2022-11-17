from s_pair import *


def break_exp():
    return pair("break", empty_pair)


def is_break(x):
    return is_pair(x) and first(x) == "break"
