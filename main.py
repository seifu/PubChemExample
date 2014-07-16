__author__ = 'sjc294@psu.edu'

import os
from BeautifulSoup import BeautifulStoneSoup


def get_files(mypath="C:\Users\ToastyDelight\Desktop\AB"):
    #This gets the file names
    f = []
    print f
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

    filelist = get_files("F:\Research\Cheminformatics\Data\PMC\AB")
    #print len(filelist)
    #print "hello"
    for t in filelist:
        soup = read_file(t)
        try:
            title = soup.find(["article-title"]).renderContents()
            year = soup.find(["year"]).renderContents()
            kwd = soup.findAll(["kwd"])
            for akwd in kwd:
                seq = (t, title, year, akwd.renderContents())
                out_text = ", ".join(seq)
                with open("PMCKwd_AB.txt", "ab") as myoutput:
                    myoutput.write(out_text+"\n")
        finally:
            soup.decompose()
