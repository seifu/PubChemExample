__author__ = 'sjc294'

import os


#fname1 = "C:\\SeifusFiles\\Research\\Cheminformatics\\Results\\ChemotherapyResults\\BMC_Public_Health_2012_Oct_30_12_930.nxml.chem"
#fname2 = "C:\\SeifusFiles\\Research\\Cheminformatics\\Results\\ChemotherapyResults\\cleaned\\clean_output_test.nxml.chem"

def get_files(mypath="C:\\Users\\ToastyDelight\\Desktop\\AB"):
    #This gets the file names
    fi = []
    for (dirpath, _, filenames) in os.walk(mypath):
        fi.extend(os.path.join(dirpath, filename) for filename in filenames)
    return fi


def clean_files(fname1,fname2):
    tx = []
    with open(fname1, 'r') as f:
        with open(fname2, 'w') as o:
            for line in f:
                temp_tx = line.split("\t")
                if len(temp_tx) in (17, 18):
                    tx = line.split("\t")
                if len(tx) < 17:
                    if len(tx) == 0:
                        tx += temp_tx
                    else:
                        tx[-1] = tx[-1].rstrip() + temp_tx.pop(0)
                        #tx.append(temp_tx)
                        tx += temp_tx
                        o.write("\t".join(tx))
                        temp_tx[:] = []
                        tx[:] = []
                else:
                    o.write("\t".join(tx))
                    temp_tx[:] = []
                    tx[:] = []

filelist = get_files("C:\\SeifusFiles\\Research\\Cheminformatics\\Results\\MissingChemotherapyPapersChemspot")

for some_file in filelist:
    clean_files(some_file,"C:\\SeifusFiles\\Research\\Cheminformatics\\Results\\MissingChemotherapyPapersChemspot_fixed_Jan9\\"+some_file.split("\\")[-1])