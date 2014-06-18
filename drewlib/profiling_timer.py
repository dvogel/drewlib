# -*- coding: utf-8 -*-

from __future__ import print_function

import time

__all__ = ['ProfilingTimer']

class ProfilingTimer(object):
    def __init__(self):
        self.prev = None

    def checkpoint(self, prefix=None):
        t = time.time()
        if self.prev is not None:
            dur = t - self.prev
            if prefix is not None:
                print(prefix, ':', sep='', end='')
            print(dur)
        self.prev = t

