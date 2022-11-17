from s_pair import *


def function(param, body):
    return pair("function", pair(param, pair(body, empty_pair)))


def is_function(x):
    return is_pair(x) and first(x) == "function"


def fun_param(f):
    return first(second(f))


def fun_body(f):
    return first(second(second(f)))
