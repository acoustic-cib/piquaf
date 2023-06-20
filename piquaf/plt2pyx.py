"""
Copyright (c) 2023, Cibby Pulikkaseril
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 

plt2gle.py - top level functions 


"""
import tempfile
from piquaf.extools import get_title, get_xlabel, get_ylabel, extract_data
from pyx import graph

def createLine2D(fig):
    """
    createLine2D

    outpath = createLine2D(fig)

    Give a figure handle in fig, this function will
    extract the relevant information and create the 
    PyX figure and 
    """
    title = get_title(fig)
    xlabel = get_xlabel(fig)
    ylabel = get_ylabel(fig)
    list_line = extract_data(fig)
    
	# create Line2D graph
    with tempfile.TemporaryDirectory() as tmpdirname:
        


"""
from pyx import *

g = graph.graphxy(width=10)
g.plot(graph.data.file("x.dat", x=1, y=2))
g.writeEPSfile("x")
	d1 key "predicted"
	d2 key "measured"
end graph

"""
