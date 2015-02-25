__author__ = 'sjc294'

import os
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

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


def missing_chemo(chemofile):
    with open(chemofile, 'r') as chemo:
        chemoread = chemo.read().splitlines()
        return chemoread


if __name__ == "__main__":

    ###home file path (linux)
    #"/media/toastydelight/5C38A5EB38A5C3FC/Data/Calcif_Tissue_Int/Calcif_Tissue_Int_2007_Dec_4_81(6)_421-429.nxml"

    ###thumbdrive file path (windows)
    #"F:\Research\Cheminformatics\Data\PMC\AB"

    ###work file path (windows)
    #"C:\SeifusFiles\Research\Cheminformatics\Data\AB\AAPS_J"

    ###last used path
    #"/media/toastydelight/5C38A5EB38A5C3FC/Data/Documents/Research/Cheminformatics/Data/CH"

    filelist = get_files("C:\\SeifusFiles\\Research\\Cheminformatics\\Data\\ChemotherapyPapersStillMissing")

    #filelist = ['C:\\SeifusFiles\\Research\\Cheminformatics\\Data\\PMC\\AB\\Acta_Radiol_Short_Rep\\Acta_Radiol_Short_Rep_2013_Nov_5_2(7)_2047981613498723.nxml']

    #filelist = missing_chemo("E:\\Research\\Cheminformatics\\Data\\MissingChemotherapyPapers.txt")

    j = len(filelist)
    i = 0
    my_stopwords = stopwords.words('english')

    for t in filelist:
        i += 1
        if i % 25 == 0:
            print(i, ' of ', j)
        #soup = read_file(t)
        soup = read_file(t)
        try:

            #if soup.find("article").attrs["article-type"] in ["review-article", "research-article"]:
                names = t.split('\\')
                article_text = soup.find(["body"]).get_text(" ")
                #outpath = "C:\\SeifusFiles\\Research\\Cheminformatics\Data\\FullText\\"+"\\".join(names[5:7])
                #outpath = "C:\\SeifusFiles\\Research\\Cheminformatics\Data\\MissingChemotherapyPapers\\"+"\\".join(names[5:7])
                #if not os.path.exists(outpath):
                #    os.makedirs(outpath)

                #remove stopwords
                content = []
                content = [w for w in article_text.split() if w.lower() not in my_stopwords]

                with open("C:\\SeifusFiles\\Research\\Cheminformatics\\Data\\ChemotherapyPapersStillMissingTrunc\\"+names[-1], "ab+") as myoutput:
                #with open("C:\\SeifusFiles\\Research\\Cheminformatics\Data\\MissingChemotherapyPapers\\"+t, "ab+") as myoutput:
                            myoutput.write(bytes(' '.join(content), 'UTF-8'))

        except Exception as ex:
            template = "an exception of type {0}. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            with open("StillMissingPMCallErrors.txt", "ab") as myoutput:
                        err_string = t + " caused " + message
                        myoutput.write(bytes(err_string+"\n", 'UTF-8'))
            continue
        finally:
            soup.decompose()