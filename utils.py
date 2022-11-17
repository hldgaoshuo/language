def log(*args, **kwargs):
    print(*args, **kwargs, flush=True)


def ensure(condition, message):
    # 在条件不成立的时候, 输出 message
    if not condition:
        log(f'*** 测试失败: {message}')
    else:
        log(f'*** 测试成功')


def ensure_equal(a, b):
    # 在条件不成立的时候, 输出 message
    if a != b:
        log(f'*** 测试失败, 希望得到({a}), 实际得到({b})')
    else:
        log(f'*** 测试成功')
