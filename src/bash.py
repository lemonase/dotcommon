#!/usr/bin/env python

from dotcommon.util import lines_starting_with
from dotcommon.crawl import crawl


def aliases(text):
    "Aliases"
    return lines_starting_with("alias ", text)


def exports(text):
    "Exports"
    return lines_starting_with("export ", text)


def ps1(text):
    "PS1"
    return lines_starting_with("PS1=", text)


def ps2(text):
    "PS2"
    return lines_starting_with("PS2=", text)


def readline_macros(text):
    "Readline macros"
    return lines_starting_with("bind ", text)


crawl("Bash", "bashrc", aliases, exports, ps1, ps2, readline_macros)
