def pair(a, b):
    return lambda select: select(a, b)


empty_pair = None


def is_pair(x):
    return callable(x)


def first(p):
    if is_pair(p):
        return p(lambda a, b: a)
    else:
        raise ValueError(f'Not a pair: ({p})')


def second(p):
    if is_pair(p):
        return p(lambda a, b: b)
    else:
        raise ValueError(f'Not a pair: ({p})')


def pair_to_string(p):
    if not is_pair(p):
        return f'{p}'
    else:
        return f'({pair_to_string(first(p))}, {pair_to_string(second(p))})'


head = first


tail = second


def map_(f, ls):
    if ls is None:
        return None
    else:
        return pair(f(head(ls)), map_(f, tail(ls)))


def append_(ls1, ls2):
    if ls1 is None:
        return ls2
    else:
        return pair(head(ls1), append_(tail(ls1), ls2))


def zip_(ls1, ls2):
    if ls1 is None or ls2 is None:
        return None
    else:
        return pair(pair(head(ls1), head(ls2)), zip_(tail(ls1), tail(ls2)))


def length_(ls):
    if ls is None:
        return 0
    else:
        return 1 + length_(tail(ls))
