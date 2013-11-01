# -*- coding: utf-8 -*-

__all__ = ['compact']

def compact(iterable):
    seq = iter(iterable)
    prev = next(seq)
    yield prev
    for item in seq:
        if item != prev:
            yield item
        prev = item

