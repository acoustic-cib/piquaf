"""
Copyright (c) 2023, Cibby Pulikkaseril
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 

extools.py - functions for extracting data from matplotlib figures.

a good reference for how containers work in Matplotlib is in
https://matplotlib.org/stable/tutorials/intermediate/artists.html#object-containers

"""
import numpy as np
import re
# from pyx.style import style.linestyle.solid, style.linestyle.dashed, style.linestyle.dotted


def get_title(fig):
    """
    title = get_title(fig)
    """
    txt = str(fig.axes)
    pattern = r"title={'center': '(.*?)'}"
    match = re.search(pattern, txt)
    out = match.group(1)
    return out


def get_xlabel(fig):
    """
    xlabel = get_xlabel(fig)
    """
    txt = str(fig.axes)
    pattern = r"xlabel='(.*?)'"
    match = re.search(pattern, txt)
    out = match.group(1)
    return out


def get_ylabel(fig):
    """
    ylabel = get_ylabel(fig)
    """
    txt = str(fig.axes)
    pattern = r"ylabel='(.*?)'"
    match = re.search(pattern, txt)
    out = match.group(1)
    return out


def extract_data(fig):
    """
    list_line = extract_data(fig)

    Loop over all lines in the figure and
    pull out all the useful information from the Line2D artist and
    dump into a dict.
    """

    list_line = []
    for this_line in fig.axes[0].lines:
        label = this_line.get_label()
        color = this_line.get_color()
        draw_style = this_line.get_drawstyle()
        line_style = this_line.get_linestyle()
        match line_style:
            case "-":
                pass
            case "--":
                line_style = 'style.linestyle.dashed'
            case ":":
                pass
        line_width = this_line.get_linewidth()
        # data
        a_a = np.array(this_line.get_data())
        g_x = a_a[0, :]
        g_y = a_a[1, :]

        list_line.append(
            {
                "label": label,
                "color": color,
                "draw_style": draw_style,
                "line_style": line_style,
                "line_width": line_width,
                "x": g_x,
                "y": g_y,
            }
        )

    return list_line
