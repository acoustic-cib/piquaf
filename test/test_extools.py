"""
Copyright (c) 2023, Cibby Pulikkaseril
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 

test_extools.py


"""
# import tempfile
# import os
import numpy as np
import matplotlib.pyplot as plt
from piquaf.extools import get_title, get_xlabel, get_ylabel, extract_data


def create_figure():
    """create_figure()
    create a sample figure
    """
    fig, a_x = plt.subplots(figsize=(5, 4))  # define fig and axes

    x_1 = np.linspace(0, 100, 100)
    y_1 = np.sin(x_1 / 10)
    y_2 = np.cos(x_1 / 8)

    a_x.plot(x_1, y_1, linewidth=1.5, label="y1")
    a_x.plot(x_1, y_2, linestyle=":", linewidth=2.5, label="y2")

    a_x.lines[0].set_color("b")
    a_x.lines[1].set_color("g")

    # add titles, x labels, y labels, legend
    a_x.set_title("It is your birthday.", fontsize=14, fontweight="bold")
    a_x.set_xlabel("Time (s)")
    a_x.set_ylabel("Voltage (V)")
    a_x.legend(fontsize=14)

    return fig


def test_get_title():
    """test_get_title(fig)"""
    fig = create_figure()
    title = get_title(fig)
    assert title == "It is your birthday.", print("get_title caused an error")


def test_get_xlabel():
    """test_get_xlabel(fig)"""
    fig = create_figure()
    xlabel = get_xlabel(fig)
    assert xlabel == "Time (s)", print("get_xlabel caused an error")


def test_get_ylabel():
    """test_get_ylabel(fig)"""
    fig = create_figure()
    ylabel = get_ylabel(fig)
    assert ylabel == "Voltage (V)", print("get_ylabel caused an error")


def test_extract_data():
    """test_extract_data(fig)"""
    fig = create_figure()
    list_line = extract_data(fig)

    label1 = list_line[0]["label"]
    label2 = list_line[1]["label"]
    color1 = list_line[0]["color"]
    color2 = list_line[1]["color"]
    ls1 = list_line[0]["line_style"]
    ls2 = list_line[1]["line_style"]
    lw1 = list_line[0]["line_width"]
    lw2 = list_line[1]["line_width"]

    assert (label1 == "y1") & (label2 == "y2"), "Error with extracting labels"
    assert (color1 == "b") & (color2 == "g"), "error with extracting color"
    assert (ls1 == "-") & (ls2 == ":"), "error with extracting linestyle"
    assert (lw1 == 1.5) & (lw2 == 2.5), "error with extracting linewidth"
