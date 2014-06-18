# -*- coding: utf-8 -*-

from drewlib.compact import compact

__all__ = ['highlight_substrings']

def highlight_substrings(subject, substrings, ansi_color=91):
    """
    Arguments:
        * subject: string within which to find substrings
        * substrings: iterable of strings to highlight
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
    # Reduce to unique matches
    substrings = list(compact(sorted(substrings)))

    # Sort longest to shortest to avoid conflicts
    substrings.sort(cmp=lambda a, b: cmp(len(b), len(a)))

    for substring in substrings:
        repl = u"\x1b[{color}m{substring}\x1b[0m".format(color=ansi_color,
                                                         substring=substring)
        subject = subject.replace(substring, repl)

    return subject

