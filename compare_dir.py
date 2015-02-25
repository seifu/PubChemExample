__author__ = 'sjc294'

import os
import shutil
import re

left_files = os.listdir("C:\\SeifusFiles\\Research\\Cheminformatics\\Data\\JanFull\\CPU7")
right_files = os.listdir("C:\\SeifusFiles\\Research\\Cheminformatics\\Data\\\JanFull\\CPU7_output")
right_files = [re.sub('\.chem', '', x) for x in right_files]

for fi in left_files:
    if fi not in right_files:
        shutil.copy("C:\\SeifusFiles\\Research\\Cheminformatics\\Data\\JanFull\\CPU7\\"+fi, "C:\\RemainingFiles5")
