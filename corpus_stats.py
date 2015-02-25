__author__ = 'sjc294'

import os
from bs4 import BeautifulSoup
import re

def get_files(mypath="C:\\Users\\ToastyDelight\\Desktop\\AB"):
    #This gets the file names
    f = []
    for (dirpath, _, filenames) in os.walk(mypath):
        f.extend(os.path.join(dirpath, filename) for filename in filenames)
    return f


def read_file(filename):
    #This reads the files and makes the soup
    #print(filename)
    f = open(filename, 'r')
    readfile = BeautifulSoup(f)
    f.close()
    return readfile


if __name__ == "__main__":

    filelist = get_files("C:\\SeifusFiles\\Research\\Cheminformatics\\Data\\PMC\\OZ")

    #filelist = ['C:\\SeifusFiles\\Research\\Cheminformatics\\Data\\IN\\Icarus\\Icarus_2011_Dec_216(2)_476-484.nxml']

    j = len(filelist)
    i = 0

    for t in filelist:
        i += 1
        if i % 100 == 0:
            print(i, ' of ', j)

        #with open("AB_names.txt", "ab+") as myoutput:
        #    myoutput.write(bytes(t+'\n', 'UTF-8'))

        soup = read_file(t)
        try:

            article_type = soup.find('article').attrs["article-type"]
            if article_type is None:
                article_type = "No Article Type"

            title = re.sub("\n", "", soup.find(["article-title"]).get_text()).replace('.', "").strip()
            title = re.sub(",", "", title)
            title = re.sub("\r", "", title)
            title = title.replace(u"\u2028", ' ')
            if title is None:
                title = "No Title"

            year = soup.find(["year"]).get_text()
            if year is None:
                year = "No Year"

            seq = (t, title, article_type, year)
            out_text = ",".join(seq)
            with open("CorpusStats_OZ.txt", "ab+") as myoutput:
                myoutput.write(bytes(out_text+"\n", 'UTF-8'))

        except Exception as ex:
            template = "an exception of type {0}. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            with open("CorpusStats_errors_OZ.txt", "ab") as myoutput:
                        err_string = t + " caused " + message
                        myoutput.write(bytes(err_string+"\n", 'UTF-8'))
            continue
        finally:
            soup.decompose()