# piquaf
A Python library that creates <b>P</b>ubl<b>I</b>cation <b>QUA</b>lity <b>F</b>igures from matplotlib figures, using the GLE (Graphics Layout Engine) compiler.

## Usage

    from tqdm import tqdm
    for i in tqdm(range(10000)):

## Installation

1. Install GLE (https://glx.sourceforge.io/) using the appropriate installer for your machine. GLE should be accessible from the command prompt.
2. 

## History of this project

When I created by PhD thesis in LaTeX, I was adamant about creating figures that would match the style of the document, and I was unhappy using figures created in MATLAB or Octave, which I used at that time. After looking for some time, I settled on GLE (https://glx.sourceforge.io/), which uses a simple format text script and text data files. 

This enabled high productivity during my thesis - all figures had source data recorded in text files, and an accompanying GLE script file. Any modifications to figures could be made easily and rapidly, just by tweaking the settings in GLE, instead of requiring to run the underlying numerical simulations. The resulting figures looked natural and clean in the LaTeX PDF:

![image](https://github.com/acoustic-cib/piquaf/assets/64725834/2c17d076-8b88-454c-bfdd-e98e941c1346)

