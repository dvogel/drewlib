# -*- coding: utf-8 -*-

import locale

__all__ = ['pretty_money']

def pretty_money(m):
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    return locale.currency(m, grouping=True)

