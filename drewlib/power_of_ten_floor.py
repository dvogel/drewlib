# -*- coding: utf-8 -*-

from __future__ import print_function

import math

__all__ = ['power_of_ten_floor']

def power_of_ten_floor(n):
    """
    Sets all but the most significant digit to zero.

    For example:
    >>> power_of_ten_floor(12517)
    10000
    >>> power_of_ten_floor(-417.6)
    -400.0
    >>> from decimal import Decimal
    >>> power_of_ten_floor(Decimal('616161'))
    Decimal('600000')
    """
    n_type = type(n)
    pow10 = n_type(pow(10, math.floor(math.log10(abs(n)))))
    return n_type(n_type(round(n / pow10)) * pow10)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

