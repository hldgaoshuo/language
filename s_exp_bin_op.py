from s_pair import *


def bin_op(op, e1, e2):
    return pair("bin_op", pair(op, pair(e1, pair(e2, empty_pair))))


def is_bin_op(x):
    return is_pair(x) and first(x) == "bin_op"


def bin_op_op(b):
    return first(second(b))


def bin_op_e1(b):
    return first(second(second(b)))


def bin_op_e2(b):
    return first(second(second(second(b))))
