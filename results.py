import csv
import itertools as it
import numpy as np
__author__ = 'sjc294@psu.edu'


def read_results(filename):
    print(filename)
    results = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            results.append(line)
    return results


def main():
    """This code expects you to read a well formatted CSV file that will be used to make an adjacency matrix. The key
    here is that the CSV has indicies according to the KWD as the final column of 4.
    """
    my_results = read_results("C:\\Users\\ToastyDelight\\PycharmProjects\\PubMedExample\\chemo_AB_results.csv")
    print(len(my_results))
    print(len(my_results[0]))
    print(my_results[0])

    #dim_size = len(my_results)
    dim_size = 4955 #This is the number of unique keywords
    mymatrix = np.zeros((dim_size, dim_size))
    #print matrix

    #test for results below. comment out when ready to use real results
    #my_results = [["file", 1, 2, 0, 0], ["file", 2, 3, 1, 1], ["f", 1, 2, 2, 2]]

    newkwd = []
    temp_file = my_results[0][0]
    for i in my_results:
        #print i
        if temp_file == i[0]:
            newkwd.extend([i[5]])
            #my_results.pop(0)
        else:
            #use list
            for item in it.product(newkwd, repeat=2):
                #print item
                mymatrix[item] += 1
                #print matrix[item]
                #print matrix[(144,144)]
            #clear list
            del newkwd[:]
            #add current to list
            newkwd.extend([i[5]])
            #update file name
            temp_file = i[0]
    #use final list
    for item in it.product(newkwd, repeat=2):
        #print item
        mymatrix[item] += 1
    #print matrix
    np.savetxt('test_chemo3.csv', mymatrix, fmt='%i', delimiter=";")

if __name__ == "__main__":
    main()
