# -*- coding: utf-8 -*-

import re

from drewlib.highlight_substrings import highlight_substrings

__all__ = ['highlighted_match']

def highlighted_match(haystack, needle, ansi_color=91):
    if isinstance(needle, (str, unicode)):
        needle = re.compile(needle, re.I)

    matches = needle.findall(haystack)
    matches = [m[0] if isinstance(m, tuple) else m
               for m in matches]

    return highlight_substrings(haystack, matches, ansi_color)

