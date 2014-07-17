import re
import os
from BeautifulSoup import BeautifulStoneSoup

__author__ = 'sjc294@psu.edu'


def get_files(mypath="C:\Users\ToastyDelight\Desktop\AB"):
    #This gets the file names
    f = []
    for (dirpath, _, filenames) in os.walk(mypath):
        f.extend(os.path.join(dirpath, filename) for filename in filenames)
    return f


def read_file(filename):
    #This reads the files and makes the soup
    print filename
    f = open(filename, 'r')
    readfile = BeautifulStoneSoup(f)
    f.close()
    return readfile


if __name__ == "__main__":
    #linux file path
    #"/media/toastydelight/5C38A5EB38A5C3FC/Data/Calcif_Tissue_Int/Calcif_Tissue_Int_2007_Dec_4_81(6)_421-429.nxml"
    #thumbdrive file path
    #"F:\Research\Cheminformatics\Data\PMC\AB"

    filelist = get_files("/media/toastydelight/5C38A5EB38A5C3FC/Data/Documents/Research/Cheminformatics/Data/CH")
    #print len(filelist)
    #print "hello"
    for t in filelist:
        soup = read_file(t)
        try:
            title = re.sub("\n", "", soup.find(["article-title"]).renderContents())
            title = re.sub(",", "", title)
            year = soup.find(["year"]).renderContents()
            kwd = soup.findAll(["kwd"])
            if len(kwd) > 0:
                for akwd in kwd:
                    seq = (t, title, year, re.sub(",", "", akwd.renderContents()))
                    out_text = ", ".join(seq)
                    with open("PMCKwdCH.txt", "ab") as myoutput:
                        myoutput.write(out_text+"\n")
        finally:
            soup.decompose()