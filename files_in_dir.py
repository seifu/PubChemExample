__author__ = 'sjc294'

import os


def get_files(mypath="C:\\Users\\ToastyDelight\\Desktop\\AB"):
    #This gets the file names
    f = []
    for (dirpath, _, filenames) in os.walk(mypath):
        #f.extend(os.path.join(dirpath, filename) for filename in filenames)
        for filename in filenames:
            with open("C:\\SeifusFiles\\Research\\Cheminformatics\\Results\\allpmcresultsjan16.txt", "ab") as my_output:
                my_output.write(bytes(filename+"\n", 'UTF-8'))
    return f


if __name__ == "__main__":
    filelist = get_files("C:\\SeifusFiles\\Research\\Cheminformatics\\Results\\AllPMCResults")
    #for item in filelist:
