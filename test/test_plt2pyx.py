"""
Copyright (c) 2023, Cibby Pulikkaseril
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 

test_plt2pyx.py
"""
import matplotlib.pyplot as plt
import numpy as np
from piquaf.plt2pyx import createLine2D


def test_createLine2D():
    fig, ax = plt.subplots(figsize=(5, 4))  # define fig and axes
    x = np.linspace(0, 100, 100)
    y1 = np.sin(x / 10)
    y2 = np.cos(x / 8)

    ax.plot(x, y1, linewidth=1.5, label="y1")
    ax.plot(x, y2, linestyle=":", linewidth=2.5, label="y2")

    ax.lines[0].set_color("b")
    ax.lines[1].set_color("g")

    # add titles, x labels, y labels, legend
    ax.set_title("It is your birthday.", fontsize=14, fontweight="bold")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Voltage (V)")
    ax.legend(fontsize=14)

    outpath = createLine2D(fig)

    assert outpath is not None, print("plt2pyx returned no path")
