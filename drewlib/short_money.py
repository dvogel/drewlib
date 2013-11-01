# -*- coding: utf-8 -*-

__all__ = ['short_money']

def short_money(n):
    sizes = [
        ('tril', 10**12),
        ('bil', 10**9),
        ('mil', 10**6),
        ('K', 10**3),
    ]
    for (label, dollars) in sizes:
        if n >= dollars:
            short_n = round(float(n) / float(dollars), 2)
            if short_n == int(short_n):
                short_n = int(short_n)
            return "${0} {1}".format(short_n, label)
    return n


