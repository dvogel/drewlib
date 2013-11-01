# -*- coding: utf-8 -*-

from operator import itemgetter

__all__ = ['freq']

def freq(xs, key):
    ftable = {}
    key = key if callable(key) else itemgetter(key)
    for x in xs:
        k = key(x)
        cnt = ftable.get(k, 0)
        ftable[k] = cnt + 1
    return ftable

