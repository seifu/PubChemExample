import re
import os
import string
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
    #print(filename)
    f = open(filename, 'r')
    readfile = BeautifulSoup(f)
    f.close()
    return readfile


if __name__ == "__main__":

    ###home file path (linux)
    #"/media/toastydelight/5C38A5EB38A5C3FC/Data/Calcif_Tissue_Int/Calcif_Tissue_Int_2007_Dec_4_81(6)_421-429.nxml"

    ###thumbdrive file path (windows)
    #"F:\Research\Cheminformatics\Data\PMC\AB"

    ###work file path (windows)
    #"C:\SeifusFiles\Research\Cheminformatics\Data\AB\AAPS_J"

    ###last used path
    #"/media/toastydelight/5C38A5EB38A5C3FC/Data/Documents/Research/Cheminformatics/Data/CH"

    filelist = get_files("C:\\SeifusFiles\\Research\\Cheminformatics\\Data\\OZ")

    #test file that has \n \r and punctuation \\Acta_Myol\\Acta_Myol_2012_May_31(1)_4-8.nxml

    #filelist = ["C:\\SeifusFiles\\Research\\Cheminformatics\\Data\\CH\\Clinics_(Sao_Paulo)\\Clinics_(Sao_Paulo)_2013_Mar_68(3)_435.nxml"]

    j = len(filelist)
    i = 0

    for t in filelist:
        i += 1
        print(i, ' of ', j)
        soup = read_file(t)
        try:
            title = re.sub("\n", "", soup.find(["article-title"]).get_text()).replace('.', "").strip()
            title = re.sub(",", "", title)
            title = re.sub("\r", "", title)
            title = title.replace(u"\u2028", ' ')

            year = soup.find(["year"]).get_text()
            kwd = soup.findAll(["kwd"])
            if len(kwd) > 0:
                for akwd in kwd:
                    #print(akwd.get_text())
                    kwd_text = re.sub(r'\W+', ' ', akwd.get_text().replace('\n', ' ').replace('\r', ''))
                    seq = (t, title, year, re.sub(",", "", kwd_text))
                    out_text = ",".join(seq)
                    #print(out_text)
                    with open("PMCKwdOZ_Oct24.txt", "ab") as myoutput:
                        myoutput.write(bytes(out_text+"\n", 'UTF-8'))
        except Exception as ex:
            template = "an exception of type {0}. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            with open("PMCKwdOZ_Oct24_errors.txt", "ab") as myoutput:
                        err_string = t + " caused " + message
                        myoutput.write(bytes(err_string+"\n", 'UTF-8'))
            continue
        finally:
            soup.decompose()