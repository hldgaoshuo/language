import inspect

from s_pair import *
from utils import log


def test1():
    p = pair(2, None)
    log(inspect.currentframe().f_code.co_name, first(p))
    log(inspect.currentframe().f_code.co_name, second(p))
    log(pair_to_string(p))


def test2():
    p = pair(2, pair(3, None))
    log(inspect.currentframe().f_code.co_name, first(p))
    log(inspect.currentframe().f_code.co_name, first(second(p)))
    log(inspect.currentframe().f_code.co_name, second(second(p)))
    log(pair_to_string(p))


def test3():
    p = pair(2, None)
    log(inspect.currentframe().f_code.co_name, head(p))
    log(inspect.currentframe().f_code.co_name, tail(p))
    log(pair_to_string(p))


def test4():
    p = pair(2, pair(3, None))
    log(inspect.currentframe().f_code.co_name, head(p))
    log(inspect.currentframe().f_code.co_name, head(tail(p)))
    log(inspect.currentframe().f_code.co_name, tail(tail(p)))
    log(pair_to_string(p))


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
