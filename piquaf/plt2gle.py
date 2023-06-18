"""
Copyright (c) 2023, Cibby Pulikkaseril
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 

plt2gle.py - top level functions 


"""
from piquaf.extools import get_title, get_xlabel, get_ylabel, extract_data


def plt2gle(fig):
    """
    PLT2GLE

    outpath = plt2gle(fig)

    Give a figure handle in fig, this function will
    extract the relevant information and write text
    files ready for GLE. Finally, it will compile with
    GLE and give you the path to the completed PDF
    """
    title = get_title(fig)
    xlabel = get_xlabel(fig)
    ylabel = get_ylabel(fig)
    list_line = extract_data(fig)


"""
!GLE file to plot MatLAB figure in Apr24_FSRDL_Pol_2_FreqResp.gle
!Created on 24-Apr-2009

size 17 13

begin graph
	size 17 13
	hscale 0.85
	vscale 0.85
	nobox
	xtitle "Frequency (MHz)" hei 0.325
	ytitle "Response (dB)" hei 0.325
	data Apr24_FSRDL_Pol_2_FreqResp_1.dat d1=c1,c2 
	data Apr24_FSRDL_Pol_2_FreqResp_2.dat d2=c1,c2 
	xaxis min 200.000 max 248.000
	yaxis min -30.000 max 0.000
	d1 line lstyle 3 color black msize 0.125
	d2 line lstyle 1 color black msize 0.125
	key pos tl nobox hei 0.400
	d1 key "predicted"
	d2 key "measured"
end graph

"""
