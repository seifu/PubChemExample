__author__ = 'sjc294'

from nltk.corpus import stopwords
import os


def get_files(mypath="C:\\Users\\ToastyDelight\\Desktop\\AB"):
    #This gets the file names
    f = []
    for (dirpath, _, filenames) in os.walk(mypath):
        f.extend(os.path.join(dirpath, filename) for filename in filenames)
    return f


if __name__ == "__main__":

    filelist = get_files("C:\\SeifusFiles\\Research\\Cheminformatics\\Data\\MissingChemotherapyPapers")
    j = len(filelist)
    i = 0
    for t in filelist:
        i += 1
        if i % 100 == 0:
            print(i, ' of ', j)

        filename = ""
        with open(t, "r", encoding="utf-8") as fi:
            _, my_filename = os.path.split(t)
            text = fi.read()
        content = []
        my_stopwords = stopwords.words('english')
        content = [w for w in text.split() if w.lower() not in my_stopwords]
        with open("C:\\SeifusFiles\\Research\\Cheminformatics\\Data\\MissingChemotherapyPapersTrunc\\" + my_filename, 'ab+') as myoutput:
            myoutput.write(bytes(' '.join(content), 'UTF-8'))