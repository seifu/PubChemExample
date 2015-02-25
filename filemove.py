#!/bin/python
import os
import shutil
#This gets the file names


def mkdir(i):
    os.mkdir("E:\\Research\\Cheminformatics\\Data\\TruncText\\INFiles"+str(i))

i = 0
j = 20000
#mypath = "/media/seifu/SeifusDrive/Research/Cheminformatics/Data/TruncText/CHTrunc"
mypath = "C:\\SeifusFiles\\Research\\Cheminformatics\\Results\\FullTextOutput"
for (dirpath, _, filenames) in os.walk(mypath):
     for filename in filenames:
    #     i += 1
    #     print(i)
    #     if i % 20000 == 0:
    #         j += 20000
    #         mkdir(j)
    #     shutil.move("E:\\Research\\Cheminformatics\\Data\\TruncText\\INTrunc\\"+filename, "E:\\Research\\Cheminformatics\\Data\\TruncText\\INFiles"+str(j))
        #print (os.path.join(dirpath,filename))
        shutil.copy(os.path.join(dirpath,filename), "C:\\SeifusFiles\\Research\\Cheminformatics\\Results\\StillMissing")