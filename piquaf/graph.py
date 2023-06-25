"""
Copyright (c) 2023, Cibby Pulikkaseril
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 

graph.py - class for holding together the details about the figure
use the same taxonomy that PyX uses

"""
from pyx import graph

class PGraph(object):
    """
    class PGraph

    abstract class for graphs
    """

    def __init__(self, width=10, height=5.9):
        """
        g = graph()
        """
        self.title = None
        self.xlabel = None
        self.ylabel = None

        self.graph_width = width
        self.graph_height = height

    def set_title(self, title):
        """
        set_title(title)

        set the top title for the figure
        """
        self.title = title

    def set_xlabel(self, xlabel):
        """
        set_xlabel(xlabel)

        set the xlabel for the figure
        """
        self.xlabel = xlabel

    def set_ylabel(self, ylabel):
        """
        set_ylabel(ylabel)

        set the ylabel for the figure
        """
        self.ylabel = ylabel

    def set_line_list(self, line_list):
        """ set_line_list(line_list)"""
        self.line_list = line_list

    def create_figure(self):
        """
        create_figure()

        in this class, create a dummy figure and store the graphics
        handle, g
        """
        self.g = graph.graphxy(width=10, 
            x=graph.axis.linear(min=0, max=50, title=self.xlabel), 
            y=graph.axis.linear(min=-0.5, max=0.5, title=self.ylabel))
        

    def write_to_file(self, filename):
        """ 
        write_to_file(filename)
        
        create an output file from graph object in self.g
        the type of file is inferred from the extension
        """
        self.g.writetofile(filename)


class PGraphLine2D(PGraph):
    """
    child class that generates a 2D line Figure
    """

    def set_line_list(self, line_list):
        """ set_line_list(line_list)"""
        self.line_list = line_list

    def create_figure(self):
        """ create_figure()"""
        # next create PxY graph
        g = graph.graphxy(width=10, 
                x=graph.axis.linear(min=0, max=50, title=self.xlabel), 
                y=graph.axis.linear(min=-0.5, max=0.5, title=self.ylabel), 
                key=graph.key.key(pos="br", dist=0.1))
        for ind, this_df in enumerate(data_file_list):
            g.plot(graph.data.file(this_df, x=1, y=2, title=list_line[ind]['label']), styles=list_line[ind]['line_style'])

        g.text(5, 5, title, [text.halign.boxcenter])
