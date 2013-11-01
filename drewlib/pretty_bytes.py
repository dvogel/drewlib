# -*- coding: utf-8 -*-

__all__ = ['pretty_bytes']

def pretty_bytes(n, sizes=['B', 'KB', 'MB', 'GB', 'TB']):
    if n >= 1024:
        return pretty_bytes(float(n) / float(1024), sizes[1:])
    else:
        return "%s %s" % (round(n, 1), sizes[0])


