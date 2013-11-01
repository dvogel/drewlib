# -*- coding: utf-8 -*-

from drewlib.compact import compact

__all__ = ['highlight_substrings']

def highlight_substrings(subject, substrings, ansi_color=91):
    # Reduce to unique matches
    substrings = list(compact(sorted(substrings)))

    # Sort longest to shortest to avoid conflicts
    substrings.sort(cmp=lambda a, b: cmp(len(b), len(a)))

    for substring in substrings:
        repl = u"\x1b[{color}m{substring}\x1b[0m".format(color=ansi_color,
                                                         substring=substring)
        subject = subject.replace(substring, repl)

    return subject

