from s_pair import *


def continue_exp():
    return pair("continue", empty_pair)


def is_continue(x):
    return is_pair(x) and first(x) == "continue"
