# -*- coding: utf-8 -*-

__all__ = ['DictSlicer']

class DictSlicer(object):
    """
    >>> DictSlicer('a', 'z')({'a': 1, 'b': 2})
    {'a': 1}
    """
    def __init__(self, *ks):
        self.ks = ks

    def __call__(self, d):
        return dict(((k, v) for (k, v) in d.iteritems() if k in self.ks))

