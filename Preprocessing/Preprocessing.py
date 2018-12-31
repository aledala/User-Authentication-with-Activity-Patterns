import sys
import numpy as np
import argparse
from sklearn import preprocessing
import pandas
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from matplotlib.dates import date2num
from matplotlib.dates import num2date
import datetime


def datestr2num(s):
    return date2num(datetime.datetime.strptime(s, "%Y-%m-%d"))

#df = np.loadtxt("steps.csv", delimiter=',', dtype=float, skiprows=1,usecols = (1,2), converters = {1: datestr2num});
#print(df)

dt = num2date(736730)
print(dt)

stepscsv = np.loadtxt("steps.csv", delimiter=',', dtype=float, skiprows=1,usecols = (1,2), converters = {1: datestr2num});
caloriescsv = np.loadtxt("calories.csv", delimiter=',', dtype=float, skiprows=1,usecols = (1,2), converters = {1: datestr2num});
minfaircsv = np.loadtxt("min_active_fairly.csv", delimiter=',', dtype=float, skiprows=1,usecols = (1,2), converters = {1: datestr2num});
minlightcsv = np.loadtxt("min_active_lightly.csv", delimiter=',', dtype=float, skiprows=1,usecols = (1,2), converters = {1: datestr2num});
minverycsv = np.loadtxt("min_active_very.csv", delimiter=',', dtype=float, skiprows=1,usecols = (1,2), converters = {1: datestr2num});

M = np.matrix(np.shape((1,6)))

M = [0] *6

#M[1] = 123
#M[2] = 22

#print(M)

#M = [0] *25
#print(M)

N = []

#print(N)

f= open("TESTDATA.txt","w+")

print(minverycsv)
print(caloriescsv)
i=0
for x in stepscsv:
    M[0] = x[0]
    f.write(str(x[0]))
    f.write(", ")
    M[1] = x[1]
    f.write(str(x[1]))
    f.write(", ")
    print(i)
    #print(caloriescsv[i,1])
    M[2] = caloriescsv[i,1]
    f.write(str(caloriescsv[i,1]))
    f.write(", ")
    M[3] = minfaircsv[i,1]
    f.write(str(minfaircsv[i,1]))
    f.write(", ")
    M[4] = minlightcsv[i,1]
    f.write(str(minlightcsv[i,1]))
    f.write(", ")
    M[5] = minverycsv[i,1]
    f.write(str(minverycsv[i,1]))
    f.write(", ")
    f.write("\n")
    N.append(M)
    M = [0] *6
    i+=1
    
##    if (first == 1):
##        M[0] = x[0]
##        f.write(str(x[0]))
##        f.write(", ")
##        f.write(str(x[1]))
##        f.write(", ")
##        M[1] = x[1]
##        first = 0
##    else:
##        f.write(str(x[1]))
##        M[j] = x[1]
##        j += 1
##        if (j%25 != 0 ):
##            f.write(", ")
##    if (j%25 == 0):
##        f.write("\n")
##        j=2
##        first = 1
##        N.append(M)
##        #print(N)
##        M = [0] *25
##        #break
        
print(N[0])
print(N[1])
print(N[2])
print(N[3])
print(N[4])

f.close()
