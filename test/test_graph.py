"""
Copyright (c) 2023, Cibby Pulikkaseril
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 

test_graph.py


"""
import os
import tempfile
from piquaf.graph import PGraph

def test_pgraph_pdf():
    """ test the PGraph class, does it execute and create a file? """
    gg = PGraph()
    gg.create_figure()
    
    with tempfile.TemporaryDirectory() as tmpdirname:
        file_path = os.path.join(tmpdirname, 'test.pdf')
        gg.write_to_file(file_path)
        outcome = os.path.isfile(file_path)

    assert outcome, print('PGraph did not successfully create %s'%filename)