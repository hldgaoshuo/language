from s_pair import *


def variable(name):
    return pair("variable", pair(name, empty_pair))


def is_variable(x):
    return is_pair(x) and first(x) == "variable"


def variable_name(v):
    return first(second(v))
