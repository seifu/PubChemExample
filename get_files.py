__author__ = 'sjc294'

import os


def get_files(mypath="C:\\Users\\ToastyDelight\\Desktop\\AB"):
    #This gets the file names
    f = []
    for (dirpath, _, filenames) in os.walk(mypath):
        f.extend(os.path.join(dirpath, filename) for filename in filenames)
    return f