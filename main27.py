import re
import os
from bs4 import BeautifulSoup

__author__ = 'sjc294@psu.edu'


def get_files(mypath="C:\\Users\\ToastyDelight\\Desktop\\AB"):
    #This gets the file names
    f = []
    for (dirpath, _, filenames) in os.walk(mypath):
        f.extend(os.path.join(dirpath, filename) for filename in filenames)
    return f


def read_file(filename):
    #This reads the files and makes the soup
    print(filename)
    f = open(filename, 'r')
    readfile = BeautifulSoup(f)
    f.close()
    return readfile


if __name__ == "__main__":

    #home file path (linux)
    #"/media/toastydelight/5C38A5EB38A5C3FC/Data/Calcif_Tissue_Int/Calcif_Tissue_Int_2007_Dec_4_81(6)_421-429.nxml"

    #thumbdrive file path (windows)
    #"F:\Research\Cheminformatics\Data\PMC\AB"

    #work file path (windows)
    #"C:\SeifusFiles\Research\Cheminformatics\Data\AB\AAPS_J"

    #last used path
    #"/media/toastydelight/5C38A5EB38A5C3FC/Data/Documents/Research/Cheminformatics/Data/CH"

    filelist = get_files("C:\\SeifusFiles\\Research\\Cheminformatics\\Data\\AB\\Anticancer_Agents_Med_Chem")
    #print len(filelist)
    #print "hello"
    for t in filelist:
        soup = read_file(t)
        try:
            title = re.sub("\n", "", soup.find(["article-title"]).get_text())
            title = re.sub(",", "", title)
            year = soup.find(["year"]).get_text()
            kwd = soup.findAll(["kwd"])
            if len(kwd) > 0:
                for akwd in kwd:
                    seq = (t, title, year, re.sub(",", "", akwd.get_text()))
                    out_text = ", ".join(seq)
                    print(out_text)
                    #with open("PMCKwdCH.txt", "ab") as myoutput:
                        #myoutput.write(out_text+"\n")
        finally:
            soup.decompose()