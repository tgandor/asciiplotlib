# -*- coding: utf-8 -*-
#
from .hist import hist
from .plot import plot
from .table import table

from .helpers import create_padding_tuple


def figure(*args, **kwargs):
    return Figure(*args, **kwargs)


class Figure(object):
    def __init__(self, width=None, padding=0):
        self._content = []
        self._width = width
        self._subfigures = None
        self._padding = create_padding_tuple(padding)
        return

    def aprint(self, string):
        self._content.append(string.split("\n"))
        return

    def show(self):
        print(self.get_string())
        return

    def get_string(self, remove_trailing_whitespace=True):
        lines = []

        padding_lr = self._padding[1] + self._padding[3]

        if self._width is None:
            width = max([len(line) for c in self._content for line in c])
            width += padding_lr
        else:
            width = self._width

        # Top padding
        lines += self._padding[0] * [" " * width]

        pr = " " * self._padding[1]
        pl = " " * self._padding[3]
        lines += [
            pl + line[: width - padding_lr] + pr for c in self._content for line in c
        ]

        # Bottom padding
        lines += self._padding[2] * [" " * width]

        if remove_trailing_whitespace:
            lines = [line.rstrip() for line in lines]

        return "\n".join(lines)

    def hist(self, *args, **kwargs):
        self._content.append(hist(*args, **kwargs))
        return

    def plot(self, *args, **kwargs):
        self._content.append(plot(*args, **kwargs))
        return

    def table(self, *args, **kwargs):
        self._content.append(table(*args, **kwargs))
        return
