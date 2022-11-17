from s_pair import *


empty_table = None


def add_table(key, value, old_table):
    return pair(pair(key, value), old_table)


def lookup_table(key, table):
    if table == empty_table:
        return empty_table
    elif first(first(table)) == key:
        return second(first(table))
    else:
        return lookup_table(key, second(table))


def length_table(table):
    return length_(table)
