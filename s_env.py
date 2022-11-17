import copy


def extend_env(k, v, env):
    m = copy.deepcopy(env)
    m[k] = v
    return m


def lookup_env(k, env):
    return env.get(k)
