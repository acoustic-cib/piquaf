
import tempfile
import os
from piquaf.extools import get_title, get_xlabel, get_ylabel, extract_data
from numpy import savetxt, column_stack, array


def createLine2D(fig):
    """
    createLine2D

    outpath = createLine2D(fig)

    Give a figure handle in fig, this function will
    extract the relevant information and create the
    PyX figure and
    """
    get_title(fig)
    get_xlabel(fig)
    get_ylabel(fig)
    list_line = extract_data(fig)

    ###########################
    # create Line2D graph
    ###########################
    cur_dir = os.path.curdir
    # first create data files for each line in list_line
    with tempfile.TemporaryDirectory() as tmpdirname:
        print(tmpdirname)

        for ind, this_line in enumerate(list_line):
            x = array(this_line["x"])
            y = array(this_line["y"])

            save_path = os.path.join(cur_dir, f"{ind:d}.dat")
            savetxt(save_path, column_stack([x, y]), fmt="%.4f", delimiter=" ")

    #########################
    ## run Pyx
    ########################
    # next create PxY graph
    g = graph.graphxy(width=10, 
                    x=graph.axis.linear(min=0, max=50, title=xlabel), 
                    y=graph.axis.linear(min=-0.5, max=0.5, title=ylabel), 
                    key=graph.key.key(pos="br", dist=0.1))
    for ind, this_df in enumerate(data_file_list):
        g.plot(graph.data.file(this_df, x=1, y=2, title=list_line[ind]['label']), styles=line_style)

    g.text(5, 5, title, [text.halign.boxcenter])

    g.writePDFfile(fname)
    return cur_dir


"""
from pyx import *

g = graph.graphxy(width=10)
g.plot(graph.data.file("x.dat", x=1, y=2))
g.writeEPSfile("x")
	d1 key "predicted"
	d2 key "measured"
end graph

"""
