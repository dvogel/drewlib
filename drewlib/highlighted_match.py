# -*- coding: utf-8 -*-

import re

from drewlib.highlight_substrings import highlight_substrings

__all__ = ['highlighted_match']

def highlighted_match(haystack, needle, ansi_color=91):
    """
    Uses the given ANSI color code to highlight substrings in
    Arguments:
        * haystack: string within which to search.
        * needle: regex (compiled or in string form) to search for.
        * ansi_color: ANSI color code
            \x1b[30m30\x1b[0m \x1b[90m90\x1b[0m
            \x1b[31m31\x1b[0m \x1b[91m91\x1b[0m
            \x1b[32m32\x1b[0m \x1b[92m92\x1b[0m
            \x1b[33m33\x1b[0m \x1b[93m93\x1b[0m
            \x1b[34m34\x1b[0m \x1b[94m94\x1b[0m
            \x1b[35m35\x1b[0m \x1b[95m95\x1b[0m
            \x1b[36m36\x1b[0m \x1b[96m96\x1b[0m
            \x1b[37m37\x1b[0m \x1b[97m97\x1b[0m
            \x1b[40m40\x1b[0m \x1b[100m100\x1b[0m
            \x1b[41m41\x1b[0m \x1b[101m101\x1b[0m
            \x1b[42m42\x1b[0m \x1b[102m102\x1b[0m
            \x1b[43m43\x1b[0m \x1b[103m103\x1b[0m
            \x1b[44m44\x1b[0m \x1b[104m104\x1b[0m
            \x1b[45m45\x1b[0m \x1b[105m105\x1b[0m
            \x1b[46m46\x1b[0m \x1b[106m106\x1b[0m
            \x1b[47m47\x1b[0m \x1b[107m107\x1b[0m
    """
    if isinstance(needle, (str, unicode)):
        needle = re.compile(needle, re.I)

    matches = needle.findall(haystack)
    matches = [m[0] if isinstance(m, tuple) else m
               for m in matches]

    return highlight_substrings(haystack, matches, ansi_color)

