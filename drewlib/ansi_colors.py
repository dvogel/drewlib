# -*- coding: utf-8 -*-

from __future__ import print_function

from itertools import chain

__all__ = ['AnsiColors']

AnsiColors = "\n".join(["\x1b[{0}m{0}\x1b[0m \x1b[{1}m{1}\x1b[0m".format(cc, cc+60)
                        for cc in chain(range(30, 38), range(40, 48))])
