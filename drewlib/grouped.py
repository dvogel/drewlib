# -*- coding: utf-8 -*-

from operator import itemgetter

__all__ = ['grouped']

def grouped(xs, key):
    groups = {}
    key = key if callable(key) else itemgetter(key)
    for x in xs:
        k = key(x)
        grp = groups.get(k, [])
        grp.append(x)
        groups[k] = grp
    return groups.values()

