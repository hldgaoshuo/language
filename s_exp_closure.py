from s_pair import *


def closure(fun, env):
    return pair("closure", pair(fun, pair(env, empty_pair)))


def is_closure(x):
    return is_pair(x) and first(x) == "closure"


def closure_fun(c):
    return first(second(c))


def closure_env(c):
    return first(second(second(c)))
