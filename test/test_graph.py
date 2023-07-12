"""
Copyright (c) 2023, Cibby Pulikkaseril
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. 

test_graph.py


"""
#
# import os
import tempfile

from piquaf.graph import PGraph


# def test_pgraph_pdf():
#     """test the PGraph class, does it execute and create a file?"""
#     gg = PGraph()
#     gg.create_figure()

#     file_list = ["test.pdf", "test.svg", "test.eps"]
#     outcome = []
#     with tempfile.TemporaryDirectory() as tmpdirname:
#         for this_file in file_list:
#             file_path = os.path.join(tmpdirname, this_file)
#             gg.write_to_file(file_path)
#             outcome.append(os.path.isfile(file_path))

#     assert all(outcome), print("PGraph did not successfully create file")


def test_tmpfile():
    gg = PGraph()
    gg.create_figure()

    FLAG_OK = False
    with tempfile.TemporaryDirectory() as tmpdirname:
        print(tmpdirname)
        file_path = "test.pdf"
        gg.write_to_file(file_path)
        FLAG_OK = True

    assert FLAG_OK, "FLAG_OK is False"
