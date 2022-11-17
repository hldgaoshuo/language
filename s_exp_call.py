from s_pair import *


def call(op, arg):
    return pair("call", pair(op, pair(arg, empty_pair)))


def is_call(x):
    return is_pair(x) and first(x) == "call"


def call_op(c):
    return first(second(c))


def call_arg(c):
    return first(second(second(c)))
