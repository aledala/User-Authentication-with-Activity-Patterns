import sys
import numpy as np
import argparse
from sklearn import preprocessing
import pandas
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


df = np.loadtxt("Hourly.csv", delimiter=',', dtype=float);
#print(df)

#M = np.matrix(np.shape((1,25)))

M = [0] *25

M[1] = 123
M[2] = 22

#print(M)

M = [0] *25
#print(M)

N = []

print(N)

f= open("TESTDATA.txt","w+")


i=0
j=2
first = 1
for x in df:
    if (first == 1):
        M[0] = x[0]
        f.write(str(x[0]))
        f.write(", ")
        f.write(str(x[1]))
        f.write(", ")
        M[1] = x[1]
        first = 0
    else:
        f.write(str(x[1]))
        M[j] = x[1]
        j += 1
        if (j%25 != 0 ):
            f.write(", ")
    if (j%25 == 0):
        f.write("\n")
        j=2
        first = 1
        N.append(M)
        #print(N)
        M = [0] *25
        #break
        
print(N[0])
print(N[1])
print(N[2])
print(N[3])
print(N[4])

f.close()
